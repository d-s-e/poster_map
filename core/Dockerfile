FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    gdal-bin proj-bin libgeos-c1v5 \
    && rm -rf /var/lib/apt/lists/*

COPY . /opt/app/
WORKDIR /opt/app/
RUN pip install --no-cache-dir -r requirements.txt


