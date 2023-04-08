FROM python:3.9-slim

SHELL ["/bin/bash", "-c"]


WORKDIR /usr/src

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 curl -y

RUN apt-get -qq update && apt-get install -y curl python3-pip && rm -rf /var/lib/apt/lists/*
# Install MinIO Client
RUN curl --silent -O https://dl.min.io/client/mc/release/linux-amd64/mc && \
    chmod +x mc && mv mc /usr/local/bin


ARG MINIO_HOST
ARG MINIO_USERNAME
ARG MINIO_PASSWORD

RUN mc alias set s3b $MINIO_HOST $MINIO_USERNAME $MINIO_PASSWORD
RUN mc cp s3b/model/best.pt best.pt

#ENV DEBIAN_FRONTEND=noninteractive
#RUN apt update && apt install software-properties-common -y
#RUN add-apt-repository ppa:deadsnakes/ppa 
#RUN apt update && apt install  --no-install-recommends  python3.9 -y

COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . .



CMD ["python3", "./app.py"]

