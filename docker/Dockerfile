# ref: https://github.com/threestudio-project/threestudio/blob/main/docker/Dockerfile

FROM nvidia/cuda:11.7.1-devel-ubuntu22.04

ENV CUDA_HOME=/usr/local/cuda
ENV PATH=${CUDA_HOME}/bin:${PATH}
ENV LD_LIBRARY_PATH=${CUDA_HOME}/lib64:${CUDA_HOME}/lib64/stubs:${LD_LIBRARY_PATH}
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

# https://pytorch.org/get-started/previous-versions/#v1130
RUN pip install torch==1.13.0+cu117 torchvision==0.14.0+cu117 --extra-index-url https://download.pytorch.org/whl/cu117

RUN pip install git+https://github.com/NVlabs/nvdiffrast.git

ENV FORCE_CUDA=1
ENV TORCH_CUDA_ARCH_LIST="8.6"
RUN pip install git+https://github.com/facebookresearch/pytorch3d.git

ENV TCNN_CUDA_ARCHITECTURES=86
RUN pip install git+https://github.com/NVlabs/tiny-cuda-nn/#subdirectory=bindings/torch

WORKDIR /gala
COPY docker/requirements.txt /gala/requirements.txt
RUN pip install -r /gala/requirements.txt

COPY . /gala
