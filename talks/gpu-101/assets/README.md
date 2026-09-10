# GPU 101 asset provenance

이 문서는 `gpu-101.tex`의 외부 자산과 자체 도식에 참고한 출처, 가공 여부를
기록한다. 기존 자산의 원본 일치는 2026-09-07에 확인했으며, 아래 역사·아키텍처·
생태계 설명의 출처는 2026-09-10에 갱신했다. 이전에 사용한 자산도 보존한다.

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
- RTX Blackwell SM: [NVIDIA RTX Blackwell GPU Architecture whitepaper](https://images.nvidia.com/aem-dam/Solutions/geforce/blackwell/nvidia-rtx-blackwell-gpu-architecture.pdf), pp. 10–12, Figure 5. 네 구획을 네 열로 펼친 자체 TikZ 도식이다. 구획별 scheduler, 64 KB register file, FP32/INT32 유닛 32개, Tensor Core 하나, load/store 유닛 네 개와 SM 공통 128 KB L1/shared memory를 표시한다. Instruction cache, dispatch, SFU, texture, RT 자원은 생략했다. 실제 면적 비율이나 배선을 재현하지 않는다.
- Resident warps: [NVIDIA Blackwell Tuning Guide, Occupancy](https://docs.nvidia.com/cuda/blackwell-tuning-guide/index.html). CC 12.0의 최대 48 warps/SM를 위 RTX Blackwell의 128 FP32/INT32 유닛과 비교한다. CC 10.0의 64 warps와 혼용하지 않는다.
- Rubin GPU: [Inside NVIDIA Rubin GPU Architecture](https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/), July 21, 2026, Figure 2 and accompanying compute, attention/softmax, memory, and NVLink descriptions. 두 compute die, NV-HBI, SM 224개, 최대 HBM4 288 GB/22 TB/s와 GPU 사이 NVLink 6를 자체 TikZ 도식으로 재구성했다. 커널→SM, 가중치/KV 버퍼→HBM4, 통신→GPU 연결망의 대응을 표시한다. GPU 내부의 NV-HBI와 GPU 사이의 NVLink는 다른 연결이다. SM 상자 수는 예시이고, 원본 이미지 복제나 정확한 floorplan 재현은 아니다. [HGX 사양](https://www.nvidia.com/en-us/data-center/hgx/)의 preliminary 표시를 따른다.
- Rubin CUDA status: [CUDA Toolkit 13.4 announcement](https://developer.nvidia.com/blog/?p=121255), September 9, 2026. `sm_107` 기능 지원은 preview이며 정식 지원은 향후 릴리스 예정이다.
- 위 출처 확인: 2026-09-10. 과거 Volta/V100 이미지 파일은 보존하지만 현재 SM/GPU 사례 슬라이드에서는 사용하지 않는다.

### Fixed-function graphics, shaders, and G80/CUDA

다음 슬라이드는 외부 그림을 추출하지 않고 자체 TikZ 도식과 수면 셰이더
의사코드를 사용한다. 고정 기능과 초기 프로그래머블 GPU의 같은 파이프라인
단계를 나란히 놓고, shader 명령→제어 회로와 레지스터↔반복 연산기를 연결한다.
G80 비교는 분리된 정점/픽셀 프로세서와 지역 레지스터·shared memory를 가진
반복 프로세서 그룹의 차이를 보여준다. 셀 수와 연결은 개념 예이며, 실제
면적·배선을 재현하지 않는다. 수면 코드는 원문 복사나 완전한 물리 모델이 아니다.

- [NVIDIA The Cg Tutorial, chapter 1](https://developer.nvidia.com/w/CgTutorial/cg_tutorial_chapter01.html), 2003, §§1.2.1–1.2.3. GeForce 256 시대의 고정 T&L, GeForce FX 시대의 정점·프래그먼트 프로그램과 계속 남아 있는 rasterizer/depth/blend 단계의 근거다. GeForce 3의 과도기적 픽셀 기능을 완전한 프래그먼트 프로그램으로 그리지 않는다.
- [Khronos ARB_fragment_shader](https://registry.khronos.org/OpenGL/extensions/ARB/ARB_fragment_shader.txt), approved June 11, 2003, Overview; [OpenGL 2.0 specification](https://registry.khronos.org/OpenGL/specs/gl/glspec20.pdf), October 22, 2004, appendix I.1, printed pp. 340–341 (PDF pages 354–355, counting from 1). 고정 texturing/color/fog 단계의 대체와 기존 ARB 확장의 core 승격을 구분한다.
- [NVIDIA Water Interaction SDK report](https://developer.download.nvidia.com/SDK/9.5/Samples/DEMOS/Direct3D9/src/WaterInteraction/docs/WaterInteraction.pdf), footer November 4, 2004, copyright 2005, PDF pp. 2–3. 셰이더로 물결에 따른 반사 왜곡을 표현하는 당시의 사례를 참고했다. 고정 기능으로는 반사나 물을 전혀 그릴 수 없었다는 의미로 사용하지 않는다.
- [GeForce 8800 GPU Architecture Technical Brief](https://www.nvidia.com/content/PDF/Geforce_8800/GeForce_8800_GPU_Architecture_Technical_Brief.pdf), November 8, 2006, printed pp. 17–18, Figure 11; pp. 20–21, Figures 12–13; pp. 22–26, Figures 14–18. 분리된 vertex/pixel 처리 경로와 통합 SP 배치, 작업 비중에 따른 활용을 비교했다. G80 통합을 GPU 전체의 단일 레지스터·메모리 풀로 표현하지 않는다.
- [CUDA Programming Guide 1.0](https://developer.download.nvidia.com/compute/cuda/1.0/NVIDIA_CUDA_Programming_Guide_1.0.pdf), June 23, 2007, printed pp. 2–5, 7, 13–15 and Figure 3-1. instruction unit·레지스터·반복 프로세서·multiprocessor별 shared memory와 장치 메모리 연결을 참고했다. 이전 그래픽 경로의 출력 제약과 CUDA의 일반 읽기·쓰기를 구분하며, G80에 현대적인 L1/L2 데이터 캐시를 추가하지 않는다.
- [Navigating GPU Architecture Support](https://developer.nvidia.com/blog/navigating-gpu-architecture-support-a-guide-for-nvidia-cuda-developers/), August 4, 2025, GPU support sections. CUDA 도입 전 하드웨어의 기능 부족과 최신 Toolkit에서 이전 CUDA 타깃의 지원이 종료되는 문제를 대본에서 구분한다.

### Workload changes, HBM, Tensor Cores, and LLM state

자체 TikZ 도식으로 메모리 패키지와 행렬 실행 경로를 각각 비교한다. 원본
이미지를 crop하지 않았으며, P100/HBM2와 Volta/Tensor Core는 역사적 사례다.
하드웨어의 개수·배선은 개념 예다. HBM에서는 일반 CUDA 읽기·쓰기를 유지하며
물리 공급 경로가 달라지고, Tensor Core에서는 지원 커널·명령과 실행 회로가
함께 달라지는 점을 구분한다.

- [Inside Pascal](https://developer.nvidia.com/blog/inside-pascal/), April 5, 2016; updated June 19, 2016, “Dramatic Improvements in Memory.” GPU 주변의 별도 GDDR5 패키지와 GPU/HBM2 스택을 같은 패키지에서 잇는 silicon interposer를 비교했다. 커널의 일반 메모리 접근과 물리 공급 경로를 구분하며, 새 HBM 전용 CUDA 인터페이스가 필요하다고 설명하지 않는다. 원문의 720/732 GB/s 수치는 사용하지 않는다.
- [Programming Tensor Cores in CUDA 9](https://developer.nvidia.com/blog/programming-tensor-cores-cuda-9/), October 17, 2017, Tensor Core introduction, cuBLAS/cuDNN, and WMMA sections. Pascal의 FMA 경로와 Volta의 행렬 곱셈·누적 명령→레지스터/Tensor Core 경로를 비교했다. CUDA 9의 라이브러리와 WMMA는 대안적인 구현 경로이며, FP16 입력·FP32 누적 사례로 한정한다. 일반 산술 유닛은 남아 있고, WMMA 호출 하나를 명령 하나나 한 사이클로 대응시키지 않는다.
- [Mastering LLM Techniques: Inference Optimization](https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/), November 17, 2023, prefill/decode, batching, KV caching, and model parallelism sections. 입력 처리와 반복 토큰 생성, 가중치·KV 상태 읽기 및 GPU 사이 통신을 자체 흐름도로 표현했다.
- [Optimizing Inference for Long Context and Large Batch Sizes with NVFP4 KV Cache](https://developer.nvidia.com/blog/optimizing-inference-for-long-context-and-large-batch-sizes-with-nvfp4-kv-cache/), December 8, 2025, “What is KV cache?” KV cache가 재계산을 줄이는 대신 메모리와 대역폭을 사용하는 소프트웨어 데이터라는 설명의 근거다. 논문의 정량 성능·정확도 주장은 사용하지 않는다.
- [NVIDIA Matrix Multiplication Background](https://docs.nvidia.com/deeplearning/performance/dl-performance-matrix-multiplication/index.html), “Math and Memory Bounds,” accessed September 10, 2026. 행렬 크기에 따라 계산과 메모리의 비중이 달라지는 점을 참고하며, LLM의 병목도 모델·배치·단계에 따라 달라진다고 한정한다.

### CUDA ecosystem

프레임워크 아래에서 라이브러리 또는 프레임워크·생성·사용자 커널로 이어지는
대표 경로를 자체 TikZ로 그렸다. 모든 연산이 모든 라이브러리를 차례로 거치는
호출 그래프가 아니다. 컴파일러와 프로파일러는 실행 경로와 구분한다.
아래 온라인 문서는 모두 September 10, 2026에 확인했다.

- [Hugging Face Transformers installation](https://huggingface.co/docs/transformers/installation): Transformers와 PyTorch의 NVIDIA GPU 실행 경로.
- [cuBLAS overview](https://developer.nvidia.com/cublas), [cuDNN documentation](https://docs.nvidia.com/deeplearning/cudnn/latest/), [NCCL documentation](https://docs.nvidia.com/deeplearning/nccl/index.html): 각각 선형대수, 신경망 연산, 여러 GPU의 collective communication 역할.
- [PyTorch backends](https://docs.pytorch.org/docs/stable/backends), [TorchInductor GPU profiling](https://docs.pytorch.org/docs/stable/user_guide/torch_compiler/torch.compiler_inductor_profiling.html), [distributed communication](https://docs.pytorch.org/docs/stable/distributed.html): 연산별 라이브러리 선택, 생성된 Triton 커널과 라이브러리 커널의 공존, CUDA/NCCL 경로.
- [CUDA platform guide](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/cuda-platform.html), §§1.3.2–1.3.4, updated September 9, 2026; [nvcc guide](https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/index.html), §§1.1.2–1.1.3: Toolkit·드라이버·런타임·컴파일의 서로 다른 역할. CUDA 생태계에 표시한 라이브러리가 모두 기본 Toolkit에 번들된다는 의미는 아니다.
- [Nsight Systems](https://developer.nvidia.com/nsight-systems), [Nsight Compute](https://docs.nvidia.com/nsight-compute/index.html): 전체 CPU/GPU 실행 흐름과 개별 커널 성능 분석.

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
