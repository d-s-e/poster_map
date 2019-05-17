#!/bin/bash

# create user:
# TODO ...

# create database:
sudo -u postgres psql -c "drop database django_poster_map;"
sudo -u postgres psql -c "create database django_poster_map owner django_poster_map;"

# create postgis extension:
sudo -u postgres psql django_poster_map -c "create extension postgis;"
