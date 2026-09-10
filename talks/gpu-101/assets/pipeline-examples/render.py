"""Render one scene at four pipeline checkpoints for the teaching slides.

Run with Python 3, NumPy and Pillow. These are original software-rasterizer
diagnostic views, not captures of an NVIDIA GPU's internal buffers.
"""

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw


OUT = Path(__file__).parent
WIDTH, HEIGHT = 640, 480
BACKGROUND = np.array([247, 249, 252], dtype=float) / 255
EYE = np.array([4.3, 3.1, 5.6])
TARGET = np.array([0, 0.65, 0])


def unit(vector):
    return vector / np.linalg.norm(vector)


FORWARD = unit(TARGET - EYE)
RIGHT = unit(np.cross(FORWARD, [0, 1, 0]))
UP = np.cross(RIGHT, FORWARD)
LIGHT = unit(np.array([-1.5, 3, 4]))


def project(points):
    relative = points - EYE
    depth = relative @ FORWARD
    focal = HEIGHT / (2 * np.tan(np.deg2rad(39) / 2))
    screen = np.column_stack((
        WIDTH / 2 + focal * (relative @ RIGHT) / depth,
        HEIGHT / 2 - focal * (relative @ UP) / depth,
    ))
    return screen, depth


def quad(points, normal, material):
    points = np.array(points, dtype=float)
    uv = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=float)
    lighting = 0.38 + 0.62 * max(0, np.dot(normal, LIGHT))
    for indices in ([0, 1, 2], [0, 2, 3]):
        yield points[indices], uv[indices], lighting, material


def scene():
    # Near orange cube first. Later, farther objects deliberately expose why
    # submission order alone cannot resolve visibility.
    a, b, top = -0.65, 0.65, 1.45
    faces = [
        ([(a, 0, b), (b, 0, b), (b, top, b), (a, top, b)], [0, 0, 1]),
        ([(b, 0, b), (b, 0, a), (b, top, a), (b, top, b)], [1, 0, 0]),
        ([(a, top, b), (b, top, b), (b, top, a), (a, top, a)], [0, 1, 0]),
    ]
    for points, normal in faces:
        yield from quad(points, normal, 'cube')
    yield from quad([(-2, 0, 1.7), (2, 0, 1.7), (2, 0, -2), (-2, 0, -2)],
                    [0, 1, 0], 'floor')
    yield from quad([(-1.55, .05, -.95), (1.05, .05, -.95),
                     (1.05, 2.05, -.95), (-1.55, 2.05, -.95)],
                    [0, 0, 1], 'glass')


TRIANGLES = list(scene())


def fragments(triangle, width, height):
    points, uv, lighting, material = triangle
    screen, depth = project(points)
    screen *= np.array([width / WIDTH, height / HEIGHT])
    x0, y0 = np.maximum(np.floor(screen.min(axis=0)).astype(int), [0, 0])
    x1, y1 = np.minimum(np.ceil(screen.max(axis=0)).astype(int), [width - 1, height - 1])
    yy, xx = np.mgrid[y0:y1 + 1, x0:x1 + 1]
    x, y = xx + .5, yy + .5
    (ax, ay), (bx, by), (cx, cy) = screen
    denominator = (by - cy) * (ax - cx) + (cx - bx) * (ay - cy)
    w0 = ((by - cy) * (x - cx) + (cx - bx) * (y - cy)) / denominator
    w1 = ((cy - ay) * (x - cx) + (ax - cx) * (y - cy)) / denominator
    w2 = 1 - w0 - w1
    inside = (w0 >= 0) & (w1 >= 0) & (w2 >= 0)
    weights = np.column_stack((w0[inside], w1[inside], w2[inside]))
    inverse_depth = (weights / depth).sum(axis=1)
    distance = 1 / inverse_depth
    interpolated_uv = (weights / depth) @ uv / inverse_depth[:, None]
    return yy[inside], xx[inside], distance, interpolated_uv, lighting, material


def shade(uv, lighting, material):
    if material == 'glass':
        return np.tile([.10, .52, .84], (len(uv), 1)), .38
    frequency = 5 if material == 'cube' else 10
    checker = np.floor(uv * frequency).astype(int).sum(axis=1) % 2
    colors = np.array([[.93, .42, .11], [1.0, .67, .23]]) if material == 'cube' else \
        np.array([[.72, .76, .80], [.94, .95, .97]])
    return colors[checker] * lighting, 1.0


def save(name, pixels):
    image = Image.fromarray(np.uint8(np.clip(pixels, 0, 1) * 255))
    image.save(OUT / name)


def wireframe():
    image = Image.new('RGB', (WIDTH, HEIGHT), tuple(np.uint8(BACKGROUND * 255)))
    draw = ImageDraw.Draw(image)
    for points, _, _, material in reversed(TRIANGLES):
        screen, _ = project(points)
        color = '#33516f' if material == 'cube' else '#91a2b4'
        positions = [tuple(p) for p in screen]
        draw.line(positions + [positions[0]], fill=color, width=2)
        for x, y in positions:
            draw.ellipse((x - 4, y - 4, x + 4, y + 4), fill=color)
    image.save(OUT / '01-vertices.png')


def coverage():
    # One center sample per deliberately enlarged cell. Count every candidate
    # fragment before visibility, including candidates at the same location.
    width, height = 40, 30
    counts = np.zeros((height, width), dtype=int)
    for triangle in TRIANGLES:
        yy, xx, *_ = fragments(triangle, width, height)
        counts[yy, xx] += 1
    image = Image.new('RGB', (WIDTH, HEIGHT), tuple(np.uint8(BACKGROUND * 255)))
    draw = ImageDraw.Draw(image)
    shades = ['#d5e1ed', '#809cb8', '#355475', '#163656']
    for y, x in np.argwhere(counts):
        draw.rectangle((x * 16 + 1, y * 16 + 1, (x + 1) * 16 - 2, (y + 1) * 16 - 2),
                       fill=shades[min(counts[y, x] - 1, 3)])
    image.save(OUT / '02-fragments.png')


def colors_and_output():
    preview = np.broadcast_to(BACKGROUND, (HEIGHT, WIDTH, 3)).copy()
    output = preview.copy()
    z_buffer = np.full((HEIGHT, WIDTH), np.inf)
    samples = [fragments(triangle, WIDTH, HEIGHT) for triangle in TRIANGLES]
    for yy, xx, depth, uv, lighting, material in samples:
        rgb, alpha = shade(uv, lighting, material)
        # Diagnostic shader-color view: overwrite in submission order, without
        # applying depth or alpha. Alpha is still computed by shade().
        preview[yy, xx] = rgb
        if alpha == 1:
            visible = depth < z_buffer[yy, xx]
            yv, xv = yy[visible], xx[visible]
            output[yv, xv] = rgb[visible]
            z_buffer[yv, xv] = depth[visible]
    # This scene has one flat transparent panel. Composite it after opaque
    # geometry, testing opaque depth and leaving that depth buffer unchanged.
    for yy, xx, depth, uv, lighting, material in samples:
        if material != 'glass':
            continue
        rgb, alpha = shade(uv, lighting, material)
        visible = depth < z_buffer[yy, xx]
        yv, xv = yy[visible], xx[visible]
        output[yv, xv] = alpha * rgb[visible] + (1 - alpha) * output[yv, xv]
    save('03-colors.png', preview)
    save('04-framebuffer.png', output)


if __name__ == '__main__':
    wireframe()
    coverage()
    colors_and_output()
