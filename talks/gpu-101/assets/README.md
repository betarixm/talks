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

하드웨어 파이프라인은 자체 TikZ 도식이며, 수면 셰이더는 자체 의사코드다.
그 앞의 단계별 예시는 아래에 기록한 자체 소프트웨어 렌더러로 생성했다.
고정 기능과 초기 프로그래머블 GPU의 같은 파이프라인
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

### `pipeline-examples/`

- Files: `01-vertices.png`, `02-fragments.png`, `03-colors.png`, `04-framebuffer.png` (각 640 × 480 pixels).
- Generator: [`pipeline-examples/render.py`](pipeline-examples/render.py), Python 3 + NumPy + Pillow. 같은 기하·카메라·제출 순서를 사용한 자체 소프트웨어 rasterizer이며 외부 이미지나 모델은 사용하지 않는다.
- Scene: 체크무늬 큐브와 바닥, 뒤쪽의 반투명 파란 판. 정점 투영, 샘플 중심의 barycentric coverage, perspective-correct UV 보간, 텍스처·조명 계산, 깊이 검사와 alpha 혼합을 실행한다.
- `01`: 변환된 정점과 삼각형 연결을 선으로 표시한 진단 화면이다. 파이프라인에 별도의 wireframe 이미지 생성 단계가 있다는 의미는 아니다.
- `02`: 40 × 30 sample grid를 확대했다. 진하기는 가려짐 처리 전 같은 위치에 생성된 프래그먼트 수이며, 하나의 최종 픽셀에 여러 후보가 있을 수 있음을 보여준다.
- `03`: 계산된 RGB를 제출 순서대로 표시하고 깊이 검사·alpha 혼합을 끈 진단 화면이다. 실제 GPU의 보편적인 중간 framebuffer라고 주장하지 않는다.
- `04`: 불투명 물체의 깊이 검사를 수행한 뒤 투명 판을 깊이 검사하고 alpha 혼합한 결과다. 판은 깊이 버퍼를 갱신하지 않는다.
- Pipeline reference: [NVIDIA The Cg Tutorial, chapter 1](https://developer.nvidia.com/w/CgTutorial/cg_tutorial_chapter01.html), §1.2.2. 논리적 설명 순서이며 early depth와 clipping 등 실제 하드웨어 최적화·세부 단계는 생략한다. 원본 그림 복제나 생성형 이미지 합성을 하지 않았다.

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

## Appendix references

아래 자료는 2026-09-10에 확인했다. 어펜딕스 구조 그림은 자체 TikZ 도식이며, Cerebras 페이지에는 아래에 기록한 공식 사진을 함께 사용한다. 반복 유닛 수, 배선, 스케줄은 별도 표시가 없으면
설명용 예시이고, 공급사 간 마케팅 성능 비교를 재현하지 않는다.

### Other accelerator ecosystems: AMD, HIP, TPU, NPUs, Cerebras

- AMD: [Q2 2017 results](https://ir.amd.com/news-events/press-releases/detail/779/amd-reports-second-quarter-2017-financial-results)는 Instinct와 ROCm 1.6의 동시 제공 사례다. ROCm이 2017년에 처음 등장했다는 뜻은 아니다. [CDNA white paper](https://www.amd.com/content/dam/amd/en/documents/instinct-business-docs/white-papers/amd-cdna-white-paper.pdf), PDF pp. 2–7은 GCN 기반 연산부, 2020년 CDNA의 행렬 실행부와 ROCm 발전의 근거다. [CDNA architecture](https://www.amd.com/en/technologies/cdna.html)는 2026년 칩렛·HBM 구조를 뒷받침한다.
- HIP: [What is HIP?](https://rocm.docs.amd.com/projects/HIP/en/latest/what_is_hip.html), [FAQ](https://rocm.docs.amd.com/projects/HIP/en/latest/faq.html). C++ 커널 언어·호스트 API와 HIPIFY를 통한 소스 이식, 수동 수정·재빌드·튜닝을 구분한다. CUDA 바이너리 호환을 주장하지 않는다. 현재 문서는 AMD 타깃을 강조하며, [6.1.2 문서](https://rocm.docs.amd.com/projects/HIP/en/docs-6.1.2/)의 NVIDIA 타깃 설명을 무조건적인 최신 지원 약속으로 옮기지 않는다.
- TPU: [Jouppi et al., ISCA 2017](https://research.google/pubs/in-datacenter-performance-analysis-of-a-tensor-processing-unit/)의 첫 세대 추론 목적과 [Google Cloud architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm), [JAX AI stack](https://docs.cloud.google.com/tpu/docs/jax-ai-stack)을 참고했다. JAX→XLA는 대표 경로이고 JAX/XLA가 TPU 전용이라는 뜻은 아니다. 배열은 선택한 행렬 경로이며 전체 칩이나 실제 Pod 배치를 재현하지 않는다.
- 추론 NPU 사례: [Furiosa SDK 2026.2](https://furiosa.ai/blog/furiosa-sdk-2026-2), [RNGD 발표](https://furiosa.ai/blog/rngd-hot-chips-press-release), [Rebellions Inference Platform](https://rebellions.ai/rebellions-product/rebellions-inference-platform/), [Optimum RBLN](https://github.com/RBLN-SW/optimum-rbln/blob/main/README.md). 컴파일러·모델 지원·서빙 스택의 역할을 참고한다. 두 회사는 추론에 집중한 예이며 모든 NPU가 같은 구조이거나 추론 전용이라고 일반화하지 않는다.
- Cerebras: [WSE-3 발표](https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine), March 2024, 90만 코어·44 GB SRAM은 **WSE-3의 역사적 예시**다. [PyTorch compiler 설명](https://www.cerebras.ai/blog/supporting-pytorch-on-the-cerebras-wafer-scale-engine), April 2022와 [weight streaming](https://training-api.cerebras.ai/en/1.9.1/wsc/cerebras-basics/cerebras-execution-modes.html)을 참고했다. MemoryX는 가중치를 스트리밍하는 학습 방식으로 한정하며, 모든 모델이 SRAM에 상주하거나 모든 추론이 MemoryX를 쓴다고 설명하지 않는다.

### LLM execution, distributed training, and networking

- 학습 상태: [ZeRO](https://arxiv.org/abs/1910.02054), 2019/2020, §§3–4. 가중치·기울기·optimizer 상태·활성값과 분할·재계산의 절충을 참고한다. 파라미터당 보편적인 바이트 수를 가정하지 않는다.
- 서빙: [PagedAttention](https://arxiv.org/abs/2309.06180), SOSP 2023와 [TensorRT-LLM chunked prefill](https://developer.nvidia.com/blog/streamlining-ai-inference-performance-and-deployment-with-nvidia-tensorrt-llm-chunked-prefill/), November 15, 2024. 동적인 KV 메모리 관리, 배칭, 첫 토큰·토큰 간 지연시간을 설명한다. 그림의 처리 순서는 자체 예시이며 실제 엔진 정책이나 성능 수치가 아니다.
- 병렬화·운영: [The Llama 3 Herd of Models](https://arxiv.org/html/2407.21783v3#S3.SS3), 2024, §3.3.2/Figure 5 및 §3.3.4. 여러 병렬화 방식의 결합, 통신·체크포인트·지연 노드·복구·전력·냉각 문제를 참고한다. 모든 장애가 전체 재시작을 요구한다는 의미는 아니다.
- 통신 계층: [NCCL overview](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/overview.html), [collectives](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html), [NVIDIA networking](https://www.nvidia.com/en-us/networking/). NCCL 소프트웨어 요청과 NVLink/NVSwitch 및 NIC·InfiniBand/Ethernet의 물리 경로를 구분한다. NVLink 영역은 서버 또는 랙일 수 있고 BlueField가 모든 GPU 전송을 통과시키는 것은 아니다.
- [Mellanox 인수 완료 발표](https://nvidianews.nvidia.com/news/nvidia-completes-acquisition-of-mellanox-creating-major-force-driving-next-gen-data-centers), April 27, 2020. 2019년 인수 발표와 완료 시점을 구분하며, 기존 NVLink 개발과 Mellanox 제품·역량의 결합을 설명한다.

### Number formats, HBM, FlashAttention, and packaging

- 숫자 형식: [Transformer Engine BF16/FP16](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/features/low_precision_training/introduction/introduction.html), Figure 1과 [TF32 설명](https://developer.nvidia.com/blog/accelerating-ai-training-with-tf32-tensor-cores/), January 27, 2021, Figures 1–2. 비트 폭은 FP32 1/8/23, FP16 1/5/10, BF16 1/8/7이며, BF16의 지수 범위와 유효 정밀도를 구분한다. TF32는 FP32 입력을 사용하는 연산 모드로 설명하고 별도의 텐서 저장 형식처럼 표시하지 않는다.
- 저정밀 계산: [Using FP8 and FP4](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/examples/fp8_primer.html), [NVFP4](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/features/low_precision_training/nvfp4/nvfp4.html), [Mixed Precision Training](https://arxiv.org/abs/1710.03740), 2017, §§2–3. 값 외의 scale 정보, 누적·민감한 계산의 정밀도와 품질 검증을 함께 다룬다. INT 양자화와 FP 형식을 구분하며 모든 연산의 무손실 교체나 고정 압축률을 주장하지 않는다.
- HBM: [Micron HBM3E](https://www.micron.com/products/memory/hbm/hbm3e)의 1,024 data I/O는 HBM3E 스택에 한정한다. 적층·TSV·interposer는 [Inside Pascal](https://developer.nvidia.com/blog/inside-pascal/)의 역사적 사례를 참고했다. FP32 덧셈의 `12 B/element`와 가상 대역폭 `4 TB/s → 0.33 TFLOP/s`는 외부 메모리에서 두 번 읽고 한 번 쓰는 **이상적 대역폭 상한**이다. 제품 실측이나 GPU 최대 연산량이 아니며 캐시 재사용·부가 비용은 생략한다.
- [FlashAttention](https://arxiv.org/abs/2205.14135), 2022, Figure 1, §3.1, Algorithm 1, Appendix B. 타일·온라인 softmax로 전체 score/probability 행렬을 HBM에 저장하지 않는 알고리즘을 설명한다. 같은 dense attention을 계산한다는 의미의 exact이며, 비트 단위 동일성·희소 근사·선형 연산량을 의미하지 않는다.
- TSMC: [CoWoS](https://3dfabric.tsmc.com/english/dedicatedFoundry/technology/cowos.htm)의 S/R/L 단면, [SoIC](https://3dfabric.tsmc.com/english/dedicatedFoundry/technology/SoIC.htm), [SoIC in depth](https://3dfabric.tsmc.com/english/dedicatedFoundry/technology/SoIC_inDepth.htm). 실리콘 interposer 단면은 CoWoS-S 예시이고, R/L까지 같은 구조로 일반화하지 않는다. SoIC의 수직 die 연결과 HBM DRAM 적층을 구분한다. [2024 Annual Report](https://investor.tsmc.com/sites/ir/annual-report/2024/2024%20Annual%20Report_E.pdf)의 “3DIC and TSMC-SoIC”를 열·통합 제약의 근거로 참고하며 특정 제품 수율이나 최신 roadmap 수치를 제시하지 않는다.

### Linux drivers and GPU containers

- [Aalto Talk with Linus Torvalds](https://www.youtube.com/watch?v=MShbP3OpASA), June 14, 2012, 약 48–50분의 Optimus/Linux 질문. 당시 지원·협력에 대한 비판을 설명하며 현재의 개인적 감정을 대변하거나 긴 직접 인용을 사용하지 않는다.
- NVIDIA [2022 kernel-module 공개](https://developer.nvidia.com/blog/nvidia-releases-open-source-gpu-kernel-modules/)와 [2024 open-module 전환](https://developer.nvidia.com/blog/nvidia-transitions-fully-towards-open-source-gpu-kernel-modules/), July 17, 2024. 커널 모듈 소스 공개, 지원 GPU에서의 기본값 변화, Linux upstream 포함 및 전체 CUDA 소프트웨어 공개를 구분한다. [저장소 README](https://github.com/NVIDIA/open-gpu-kernel-modules)의 모듈·GSP firmware·user-space 버전 관계도 유지한다.
- [Container Toolkit concepts](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/1.10.0/concepts.html)의 Motivation/Background와 [CUDA compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/why-cuda-compatibility.html). 애플리케이션 user space와 호스트 드라이버를 분리하는 원리를 참고하며, 과거 문서를 현재 설치 절차로 사용하지 않는다. 이미지 이동이 하드웨어·드라이버 호환성이나 동일한 성능·수치 결과를 보장하지 않는다.
- 현재 연결 방식: [Architecture overview](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/arch-overview.html), [CDI support](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/cdi-support.html), [prerequisites](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html). 장치 노드·드라이버 구성요소를 연결하는 toolkit/runtime/CDI와 호스트 커널 드라이버의 경계를 설명한다. 예시는 일반 Linux 컨테이너와 각각 할당된 물리 GPU이며, 가시성 설정을 자동 분할·성능 격리로 표현하지 않는다.

### PyTorch/XLA, PJRT, and StableHLO

- [PyTorch/XLA 2.4 — XLA Tensor Deep Dive](https://docs.pytorch.org/xla/release/r2.4/index.html): lazy graph capture, graph execution and compilation reuse. The diagram is a classic path, not a claim about every execution mode. [TorchTPU announcement](https://developers.googleblog.com/torchtpu-running-pytorch-natively-on-tpus-at-google-scale/), April 22, 2026, supplies the dated note about subsequent native integration work.
- [PJRT migration documentation](https://docs.pytorch.org/xla/release/r2.4/runtime.html), opening milestones and Benefits: TensorFlow-based XRT, gRPC overhead, 2.0 default when XRT is not configured, 2.1 stable, and the TPU implementation in libtpu. The before/after runtime diagram is conceptual; it does not claim that all host communication disappeared or that all models improve by a fixed percentage.
- [OpenXLA PJRT](https://openxla.org/xla/pjrt) and [C++ API overview](https://openxla.org/xla/pjrt/cpp_api_overview): device-specific implementations behind a shared API for device discovery, buffers, compile/load and execution. PJRT is separate from the program representation and can invoke compilation rather than only dispatching already-compiled code.
- [OpenXLA PyTorch Conference 2022 poster](https://pytorch.s3.amazonaws.com/posters/ptc2022/H01.pdf), p. 1: lack of versioning/compatibility guarantees for HLO/MHLO. [StableHLO](https://openxla.org/stablehlo), [roadmap](https://openxla.org/stablehlo/roadmap) and [compatibility](https://openxla.org/stablehlo/compatibility): specified ops, serialization, H1 2024 v1.0 and the scope of artifact compatibility. Internal HLO remains; custom-call semantics and target performance are not universal portability guarantees.
- [Torch Export to StableHLO, 2.6](https://docs.pytorch.org/xla/release/r2.6/features/stablehlo.html) is the concrete export example. Do not imply that every torch_xla runtime call first exports a serialized artifact. These are original TikZ diagrams, with no external image extraction. Sources checked 2026-09-10.

### Cerebras wafer-scale processor photograph

- File: `cerebras-wafer-in-hands.png` (4096 × 2160, original PNG).
- Source page: [Cerebras — Chip](https://www.cerebras.ai/chip), accessed 2026-09-10.
- Original asset: [Cerebras CDN photo](https://cdn.sanity.io/images/e4qjo92p/production/2e3644fdc0293fc7d6ca2933f35eba4128e39b12-4096x2160.png).
- Treatment: aspect ratio preserved; no crop, recoloring, retouching, or generated content. The person's hands and entire processor remain visible for scale. Credit: Cerebras.
- The photo illustrates physical wafer scale; its generation is not inferred from appearance. The adjacent WSE-3 / 2024 / 900,000 cores / 44 GB SRAM labels describe the separately cited historical architecture example.

### AlexNet: the workload transition in the main talk

- [Krizhevsky, Sutskever & Hinton, ImageNet Classification with Deep Convolutional Neural Networks (2012)](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf): PDF p. 3, §3.2 documents the two-GPU split, 3 GB per GTX 580 and selected-layer communication; p. 5, Figure 2 shows the network partition; p. 7, §§5–6 gives roughly 5–6 days per network and competition results. The slide does not equate one trained CNN with the winning multi-model entry or present a new benchmark.
- [Original AlexNet source code, Computer History Museum](https://github.com/computerhistory/AlexNet-Source-Code): primary-source archive for the researchers' CUDA implementation. No code or external figure is copied into the slide; it uses an original TikZ schematic with illustrative SM counts and network partitions.
- Narrative scope: a landmark use of existing GPU compute before the later P100/HBM2 and Volta/Tensor Core examples. Memory capacity, memory bandwidth, and cross-GPU communication remain separate constraints. Do not identify AlexNet as the first GPU-trained network or the sole cause of subsequent hardware features. Sources checked 2026-09-10.
