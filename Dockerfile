FROM python:3.8-slim

RUN apt-get update && apt-get install gcc -y && apt-get clean

WORKDIR /app

ENV PYTONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY src/ src/
