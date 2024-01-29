# ref: https://github.com/threestudio-project/threestudio/blob/main/docker/Dockerfile

FROM nvidia/cuda:11.7.1-devel-ubuntu22.04

ENV CUDA_HOME=/usr/local/cuda
ENV PATH=${CUDA_HOME}/bin:${PATH}
ENV LD_LIBRARY_PATH=${CUDA_HOME}/lib64:${LD_LIBRARY_PATH}
ENV LIBRARY_PATH=${CUDA_HOME}/lib64/stubs:${LIBRARY_PATH}

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    libegl1-mesa-dev \
    libgl1-mesa-dev \
    libgles2-mesa-dev \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    python-is-python3 \
    python3.10-dev \
    python3-pip \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip setuptools ninja

# FIXME: cudnn 설치하거나 설치된 이미지 사용하도록 수정해야 함
# https://pytorch.org/get-started/previous-versions/#v1130
RUN pip install torch==1.13.0+cu117 torchvision==0.14.0+cu117 --extra-index-url https://download.pytorch.org/whl/cu117

RUN pip install git+https://github.com/NVlabs/nvdiffrast.git

ENV FORCE_CUDA=1
ENV TORCH_CUDA_ARCH_LIST="8.6"
RUN pip install git+https://github.com/facebookresearch/pytorch3d.git

# for RTX 30xx
# ENV TORCH_CUDA_ARCH_LIST="8.6"
# ENV TCNN_CUDA_ARCHITECTURES=86
# for RTX 40xx
ENV TORCH_CUDA_ARCH_LIST="8.9"
ENV TCNN_CUDA_ARCHITECTURES=89
RUN pip install git+https://github.com/NVlabs/tiny-cuda-nn/#subdirectory=bindings/torch

COPY docker/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
