#!/bin/bash

cd /app/task_geru/task_geru

gunicorn app:app --bind 0.0.0.0:5000 -w 4 --reload --access-logfile -
