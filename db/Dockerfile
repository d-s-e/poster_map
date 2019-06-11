FROM postgres:11

RUN apt-get update && apt-get install -y \
    postgis \
    && rm -rf /var/lib/apt/lists/*

COPY ./01-setup_db.sh /docker-entrypoint-initdb.d/
