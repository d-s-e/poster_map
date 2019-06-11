#!/usr/bin/env bash

python3 manage.py migrate --no-input --no-color
python3 manage.py loaddata initial_posterdata --no-color
python3 manage.py collectstatic --no-input --no-color

gunicorn poster_map.wsgi:application --bind 0.0.0.0:8000 --workers=2 --threads=4 --worker-class=gthread --worker-tmp-dir /dev/shm

