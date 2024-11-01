#!/bin/bash

sleep 10
pipenv sync -v
celery -A worker worker -l info
