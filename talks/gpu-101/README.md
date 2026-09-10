# GPU 101

그래픽과 AI의 요구에 따라 GPU 하드웨어와 CUDA가 함께 발전한 과정을 다루는 입문 발표.
영어 본문 51장, 선택형 부록 19장과 한글 발표 대본으로 구성되어 있다.
SM 내부는 RTX Blackwell, GPU 전체 사례는 Rubin 공개 예비 사양을 사용한다
(2026-09-10 기준, Rubin CUDA 지원은 13.4 프리뷰).

## 내용

- 고정 기능·셰이더 프로세서 비교, GPGPU와 G80/CUDA 실행 경로
- Thread, warp, block, grid와 SM의 관계
- GDDR5/HBM 패키지와 일반 산술/Tensor Core 경로 비교, AI 요구와 Rubin
- PyTorch와 CUDA 라이브러리·커널·개발 도구의 관계
- CPU–GPU 데이터 전송, 캐시, shared memory, 레지스터
- 벡터 덧셈으로 따라가는 커널 실행과 결과 저장
- 부록: AMD·HIP·TPU·NPU·Cerebras, LLM과 데이터센터·네트워킹,
  숫자 형식·HBM·FlashAttention·TSMC 패키징, Linux와 GPU 컨테이너

부록은 주제별 바로가기 목차를 제공한다. 각 부록 슬라이드 상단의
`Appendix index`로 목차에 돌아갈 수 있다.

## 파일

- [슬라이드](gpu-101.pdf) · [발표자용 PDF](gpu-101-notes.pdf)
- [원고](gpu-101.md) · [Beamer 소스](gpu-101.tex)
- [이미지 출처](assets/README.md) · [편집 지침](AGENTS.md)
