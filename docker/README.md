# 도커 이미지 생성 및 실행 테스트 메모

1. 베이스 이미지 생성

    ```bash
    $ docker build -f docker/Dockerfile -t gala_env ./
    ```

    - pytorch 2.2.0(cu118) + xformer 설치한 이미지를 사용하려면 `Dockerfile_cu118_pt220_xformers` 파일로 이미지 생성 (정확한 원인은 모르겠지만, RTX 4090은 pytorch 1.13.0 으로 실행했을 때 텍스쳐 단계에서 메모리 부족으로 터지는데 2.2.0 이미지로 실행할 경우 안터지고 잘 동작하는 것 같음)
    - RTX 4090, A6000 GPU 에서 테스트. 다른 GPU 사용시에는 `TORCH_CUDA_ARCH_LIST="8.6"`, `TCNN_CUDA_ARCHITECTURES=86` 환경변수를 적절한 [Compute Capability](https://developer.nvidia.com/cuda-gpus#compute) 에 맞춰 수정해야 함...

2. 이미지 실행 및 setup.sh 실행

    ```bash
    # 실행 종료 후 도커 컨테이너를 유지하려면 `--rm` 플래그 제거하고 이미지 실행
    $ docker run -it --rm --gpus all gala_env bash

    # 이후 도커 이미지 안에서
    $ bash docker/setup.sh
    ```

3. 이후 [README.md](../README.md) 에 setup.sh 실행 뒷부분 설명을 쭉 따라서 실행(도커 이미지 안에서)

