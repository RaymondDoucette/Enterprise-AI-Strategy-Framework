# Use NVIDIA CUDA base image for high-performance AI
FROM nvidia/cuda:12.2.0-base-ubuntu22.04

# Set professional metadata
LABEL maintainer="Raymond Doucette"
LABEL version="1.0.0"
LABEL description="Enterprise AI Strategy Framework - Instruction & Advisory Environment"

# Install system dependencies
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    python3.10 python3-pip git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# Install core advisory and instruction dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy framework files
COPY . .

CMD ["/bin/bash"]
