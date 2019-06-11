#!/usr/bin/env bash

echo "creating django user"
psql -c "create user django_poster_map with password 'M3t}+FJa]|yWHVa%S@(=Mv&n';"

echo "creating django database"
psql -c "create database django_poster_map owner django_poster_map;"

echo "creating postgis extension"
psql django_poster_map -c "create extension postgis;"
