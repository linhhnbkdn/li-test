#!/bin/bash

python -m celery -A worker worker -l info
