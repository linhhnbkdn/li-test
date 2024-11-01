#!/bin/bash

sleep 10
python manage.py migrate
python manage.py import_seed
python manage.py runserver 0.0.0.0:4011
