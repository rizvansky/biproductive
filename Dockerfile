FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /biproductive
COPY requirements.txt /biproductive/
RUN pip install -r requirements.txt
COPY . /biproductive/
