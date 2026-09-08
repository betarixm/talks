# GPU 101 asset provenance

이 문서는 `gpu-101.tex`에서 실제로 참조하는 외부 자산의 출처와 가공 여부를
기록한다. 출처와 원본 일치는 2026-09-07에 확인했다.

저장소의 라이선스가 아래 제3자 자산에 자동으로 적용되는 것은 아니다. 이미지에서
재배포를 명시적으로 허용하는 오픈 라이선스를 확인하지 못했다. 공개 저장소에
배포하려면 각 권리자의 조건과 적용 가능한 예외를 별도로 확인하거나, 출처만
참고해 독자적인 TikZ 그림으로 교체한다. 폰트는 이 디렉터리에 중복 번들하지
않고 저장소 루트 `fonts/`와 TeX Live의 `unfonts-core`를 사용한다.

## NVIDIA NVISION 08 / MythBusters thumbnail

### `mythbusters-gpu-cpu.jpg`

- [Source video](https://www.youtube.com/watch?v=8_ZTvG1WQxM)
- [Direct thumbnail](https://i.ytimg.com/vi/8_ZTvG1WQxM/maxresdefault.jpg)
- Current uploader: HOSTKEY
- Underlying footage: NVIDIA NVISION 08, August 2008
- Local processing: 없음. YouTube thumbnail과 byte-for-byte 동일하다.

현재 영상은 NVIDIA 공식 채널이 아닌 HOSTKEY의 재업로드다. 원 시연과 현재
업로더를 구분해 표기하며, 다운로드 가능한 thumbnail이라는 사실을 재배포
허가로 해석하지 않는다.

## NVIDIA Corporate Timeline

공통 출처: [NVIDIA corporate timeline](https://www.nvidia.com/en-us/about-nvidia/corporate-timeline/)

세 파일 모두 위 페이지가 제공하는 원본 JPEG와 byte-for-byte 동일하고 별도
가공하지 않았다.

### `nvidia-1993-3d-graphics.jpeg`

- Timeline entry: 1993 — 3D Graphics
- [Direct image](https://www.nvidia.com/content/nvidiaGDC/us/en_US/about-nvidia/corporate-timeline/_jcr_content/root/responsivegrid/copy_of_nv_carousel__292630713/item_1669209935575.coreimg.jpeg/1688446141198/nvidia-timeline-3d-graphics-1993.jpeg)

### `nvidia-1999-gpu.jpeg`

- Timeline entry: 1999 — GPU
- [Direct image](https://www.nvidia.com/content/nvidiaGDC/us/en_US/about-nvidia/corporate-timeline/_jcr_content/root/responsivegrid/copy_of_nv_carousel__292630713/item_1669209940663.coreimg.jpeg/1688446141218/nvidia-timeline-gpu-1999.jpeg)

### `nvidia-2006-cuda.jpeg`

- Timeline entry: 2006 — CUDA
- [Direct image](https://www.nvidia.com/content/nvidiaGDC/us/en_US/about-nvidia/corporate-timeline/_jcr_content/root/responsivegrid/copy_of_nv_carousel__292630713/item_1669209938611.coreimg.jpeg/1688446141370/nvidia-timeline-cuda-2006.jpeg)

이 자산은 현재 timeline의 공식 마케팅 이미지이지, 각 연도에 제작된 사료라는
의미로 사용하지 않는다. 이용 조건은 [NVIDIA Terms of Service](https://www.nvidia.com/en-us/about-nvidia/terms-of-service/)를
확인한다.

## NVIDIA CUDA Programming Guide figures

아래 PNG는 NVIDIA 문서 서버의 원본과 byte-for-byte 동일하고 crop하지 않았다.

### `nvidia-grid-of-thread-blocks.png`

- Figure: Grid of Thread Blocks
- [Source section](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html#thread-hierarchy-grid-of-thread-blocks)
- [Direct image](https://docs.nvidia.com/cuda/cuda-programming-guide/_images/grid-of-thread-blocks.png)

CUDA Programming Guide와 그림은 NVIDIA 저작권 자료이며 오픈 콘텐츠
라이선스가 표시되어 있지 않다. 재사용 시 figure 이름과 원문 링크를 유지하고,
NVIDIA의 후원이나 보증을 암시하지 않는다. 관련 조건은 [CUDA Toolkit EULA](https://docs.nvidia.com/cuda/eula/index.html)와
NVIDIA Terms of Service를 확인한다.

## TikZ redraw references

로컬 raster를 복제하지 않고 개념만 덱의 공통 선·간격 문법으로 다시 그린
슬라이드도 원문 링크를 slide credit에 유지한다.

- Block scheduling: [NVIDIA CUDA Programming Guide, Thread block scheduling](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html#thread-block-scheduling)
- Warp width versus execution width: Stanford CS149, Fall 2025, slide 45

## Stanford CS149 lecture crops

공통 원본:

- Course: Stanford CS149, Parallel Computing, Fall 2025
- Lecture 7: GPU Architecture & CUDA Programming
- [Course page](https://gfxcourses.stanford.edu/cs149/fall25/)
- [Source PDF](https://gfxcourses.stanford.edu/cs149/fall25content/media/gpuarch/07_gpuarch.pdf)

아래 PNG는 PDF 페이지를 래스터화한 뒤 발표에 필요한 영역만 crop한 파생
이미지다. 원본의 Stanford footer가 crop에서 제거되었으므로 덱의 별도 source
credit을 유지한다. PDF 페이지는 1부터 센다.

### `stanford-rendering.png`

- PDF page 5; [full slide JPEG](https://gfxcourses.stanford.edu/cs149/fall25content/media/gpuarch/images/slide_005.jpg)
- Content: wireframe teapot → rendered teapot
- Additional credit in the source and crop: Henrik Wann Jensen

### `stanford-shader.png`

- PDF page 13; [full slide JPEG](https://gfxcourses.stanford.edu/cs149/fall25content/media/gpuarch/images/slide_013.jpg)
- Content: annotated GLSL fragment shader and texture-coordinate diagram

### `stanford-v100-gpu.png`

- PDF page 52; [full slide JPEG](https://gfxcourses.stanford.edu/cs149/fall25content/media/gpuarch/images/slide_052.jpg)
- Content: V100 GPU, 80 SMs, L2 cache, and HBM hierarchy

Stanford 강의 자료에서 명시적인 오픈 라이선스를 확인하지 못했다. 공개 열람
가능하다는 사실만으로 crop의 공개 저장소 재배포가 허용되는 것은 아니다.

## Publication checklist

- [ ] Stanford crop을 쓴 슬라이드에 PDF URL과 slide 번호를 유지한다.
- [ ] `stanford-rendering.png` 안의 Henrik Wann Jensen credit을 유지한다.
- [ ] NVIDIA figure를 쓴 슬라이드에 정확한 guide/timeline URL을 유지한다.
- [ ] NVIDIA 또는 Stanford가 발표를 후원·보증한다는 인상을 주지 않는다.
- [ ] 공개 배포 전, 오픈 라이선스가 없는 이미지는 허가를 받거나 TikZ로 교체한다.

## Complete Stanford vector crops (2026-09-08)

아래 두 파일은 위 Stanford CS149 원본 PDF에서 해당 페이지를 추출한 뒤
MediaBox와 CropBox만 조정했다. 그림·문자·주석 자체는 수정하지 않았으며,
벡터 도형과 임베디드 폰트를 유지한다. 기존 PNG는 보존했다. 제목과 강의
footer가 crop 밖에 있으므로 사용하는 슬라이드에 강의명, PDF URL과 page
번호를 별도로 표시한다. 위 Stanford 자산의 권리 및 출처 설명이 동일하게
적용된다.

### `stanford-v100-complete.pdf`

- Source: PDF page 52, “NVIDIA V100 GPU (80 SMs)”
- Content: 전체 80 SM 도식, L2 cache, 대역폭 화살표와 16 GB HBM 상자를 포함한다.
- Crop: 원본 1920 × 1080 pt 페이지의 `(325, 20, 1625, 955)` 영역
  (PDF 좌표계; 왼쪽, 아래, 오른쪽, 위).
- Result: 1300 × 935 pt. 기존 `stanford-v100-gpu.png`에서 잘렸던 하단 HBM
  상자와 레이블을 포함하며, 상단 제목의 잘린 일부는 남기지 않는다.

### `stanford-shader-complete.pdf`

- Source: PDF page 13, “Example shader program”
- Content: GLSL 예제, texture-coordinate 도식, 입력·함수·출력 주석.
- Crop: 원본 1920 × 1080 pt 페이지의 `(65, 78, 1640, 935)` 영역
  (PDF 좌표계; 왼쪽, 아래, 오른쪽, 위).
- Result: 1575 × 857 pt. 기존 PNG에서 잘렸던 출력 주석과 화살표를 포함한다.
- Reading note: 원본에서 “pixel”이라고 축약해 표현하는 부분은 발표에서
  fragment와 최종 pixel의 차이를 설명한다. 코드 상세를 설명하려면 넓게
  배치하고, 개념 설명만 필요하다면 덱의 자체 코드·도식이 더 읽기 쉽다.
