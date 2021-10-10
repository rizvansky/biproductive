FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /biproductive

# Install weasyprint dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      python3-dev \
      python3-pip \
      python3-cffi \
      libcairo2 \
      libpango1.0-0 \
      libgdk-pixbuf2.0-0 \
      libffi-dev \
      shared-mime-info && \
      apt-get -y clean && \
      rm -rf /var/lib/apt/lists/*
COPY requirements.txt /biproductive/
RUN pip install -r requirements.txt
COPY . /biproductive/
