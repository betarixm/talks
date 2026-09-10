# GPU 101 working instructions

## Scope and source of truth

These instructions apply to this directory and its descendants. Follow the
user's current instructions when they change the choices recorded here.

- Read `gpu-101.md` and the relevant frames in `gpu-101.tex` before changing
  the narrative. Preserve the manuscript's progression from graphics to
  general-purpose compute, the execution engine, and the `A + B` example.
- Build the execution-engine story from warps to the resources they need:
  register files, execution state, schedulers, and execution units. Then
  propose one giant GPU-wide pool, show its data and control connection
  costs, and introduce SMs as local groups of those resources. Omit the
  standalone warp-divergence explanation.
- Define a warp consistently as a hardware-managed group of 32 logical
  threads. Introduce required roles before choosing resource counts and
  connections. Label scheduler output as selected instructions and use
  repeated cells for execution-unit groups so a category does not look like
  one physical unit.
- Preserve the requested extensions: host-to-device input transfer,
  cache/register access, optional shared-memory staging, contents, section
  dividers, and the closing disclaimer.
- Keep visible slides in English and spoken narration in Korean `\note`.
  Include notes on title, contents, section-divider, and closing pages too.
  Write natural narration that explains the figure and connects adjacent
  slides, rather than merely translating the visible labels.
- Keep presentation content in `gpu-101.tex`. The `gpu-101-notes.tex` wrapper
  builds the same source with the English slide on the left and Korean
  narration on the right.

## Layout and navigation

Use `../../styles/default.sty` and `../exploit-bench/exploit-bench.tex` as the
style reference: white 16:9 pages, local Inter fonts, black headings, gray
section labels, generous margins, and a ruled footer. Prefer local changes
for talk-specific needs so other presentations retain their styling.

- Reuse the shared `\titlepage`, `\tocframe`, and `\sectionframe` templates.
  Section dividers highlight the current section and fade surrounding ones.
- Preserve the closing disclaimer's top title/subtitle, bottom explanation,
  hairline, and three-column contact footer. Keep it as the final slide.
- Preserve the intentional spoken ending: the narrative conclusion says
  thank you, then the final slide gives the full disclaimer narration.
  The user explicitly confirmed this sequence; do not shorten or move the
  final narration to eliminate the second ending.
- When adding or reordering sections, update the Korean narration selected
  by `\AtBeginSection` and its `\ifcase` mapping in `gpu-101.tex`.
- Give each content frame one main point. Prefer photos, assets, and diagrams
  when they explain the point well. Use ordinary bullets for concise facts
  or constraints; do not force prose into elaborate cards.

## Semantic palette

| Role | Main | Background | Border | Shape convention |
| --- | --- | --- | --- | --- |
| Logical work: thread, warp, block, kernel | `#1E40AF` | `#EFF6FF` | `#93C5FD` | Blue, dashed outline |
| Hardware: SM, scheduler, execution unit | `#26713D` | `#F0F8F0` | `#9CCAA5` | Green, solid outline |
| Stored data: buffers, registers, cache | `#A35A12` | `#FFF7E9` | `#E4BD85` | Amber, solid outline |
| Context, inactive items, explanatory text | `#666666` | near-white | `#CDD2D8` | Gray |

Reuse this palette consistently. Carry meaning through labels and line
styles as well as color. A blue cell denotes a logical item, not a physical
ALU. Keep external figures' original palettes and identify them as sourced
examples; do not silently recolor them into the schematic vocabulary.

## Reusable components

Use the existing helpers before introducing new layout machinery:

- `diagram`: a 14.8 cm canvas with explicit height, usually 4.2–4.6 cm.
- `workbox`, `hwbox`, `membox`, `plainbox`: semantic TikZ styles with 2 pt
  corners, 0.7 pt outlines, and no shadows.
- `flow`: restrained gray arrows; amber arrows can emphasize data movement.
- `takeaway`: one bold sentence underneath a figure, when useful.
- `credit`: a clickable source line in a reserved strip above the footer.
- `compactitems`: short, ordinary bullets for constraints and qualifications.
- `listings`: readable monospaced code on a quiet gray background.

Use repeated cells for repeated work, nested boundaries for containment,
and timelines for sequencing. Treat the measurements above as defaults,
not fixed limits. Aim for 9–11 pt diagram text; reserve tiny type for indices
and source credits. Use large numbers where scale matters. Keep content
clear of the source-credit strip and footer, and avoid shrinking text to
compensate for an overcrowded layout.

## Technical accuracy

- Present the SM construction as a design thought experiment, not the
  literal historical order of GPU invention.
- Label the `4096 × 256` launch as a teaching implementation with one element
  per thread, not PyTorch's actual optimized kernel configuration.
- Distinguish logical work, resident work, execution width, and physical
  resources. Label illustrative schedules and resource-limit assumptions.
- Scope the detailed SM diagram and residency example to RTX Blackwell (CC 12.0).
  The whole-GPU example uses Rubin public preliminary specifications as of
  2026-09-10; CUDA 13.4 support is preview. Do not transplant Blackwell internal
  counts to Rubin or infer instruction latency from unit counts.
- Preserve the distinction between host return and GPU completion. Show
  same-stream ordering and direct writes into the GPU result buffer.
- Separate CPU-to-GPU input transfer from on-device loads. The original
  `torch.randn(device="cuda")` does not require a CPU input copy.
- Distinguish global buffers, GPU-wide L2, SM-local L1, block shared memory,
  and private thread register values. Shared memory is optional explicit
  staging; a warp is not another memory tier. Qualify cache paths by policy
  and architecture rather than implying every access traverses every level.

## Assets and documentation

- Record source URLs, source page numbers, and extraction or cropping details
  in `assets/README.md` when adding or changing external assets.
- Retain visible source credits and original image credits. Check that crops
  preserve the relevant diagram and labels before using them.
- Keep existing assets unless their removal is part of the requested work.
- Keep `README.md` brief: summarize the topic and link the main files.
  Omit build instructions, user-request history, and implementation diaries.
  Update factual metadata such as the slide count when the output changes;
  it is not a fixed deck-length requirement.

## Build and verification

For TeX, asset, font, or layout changes, build both PDFs from this directory:

```bash
latexmk -lualatex -interaction=nonstopmode -halt-on-error gpu-101.tex gpu-101-notes.tex
```

Use the repository's Inter fonts and the existing UnDotum/DejaVu font setup.
If the TeX font cache is not writable, point `TEXMFVAR` and `TEXMFCACHE` at
a writable directory.

- Inspect build logs for errors, missing glyphs, and overfull boxes.
- Render and inspect changed slides and their note pages for overlap,
  clipping, legibility, and complete Korean narration.
- For navigation changes, also check the contents page, each section divider,
  current-section highlighting, corresponding notes, and the final page.
- Confirm that audience and speaker PDFs have matching page counts and that
  Korean narration is absent from the audience PDF.
- Keep both PDFs in sync with presentation changes. Documentation-only edits
  do not require rebuilding the deck.
