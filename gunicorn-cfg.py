# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - present deplooymentsoftware@gmail.com
"""
import multiprocessing

bind_oh_sansi = '0.0.0.0:8000'
bind_backoffice = '0.0.0.0:8001'
workers = multiprocessing.cpu_count() * 2
accesslog = '-'
loglevel = 'debug'
capture_output = True
enable_stdio_inheritance = True

oh_sansi_cmd = 'gunicorn -c gunicorn-cfg.py apps.oh_sansi:app'
backoffice_cmd = 'gunicorn -c gunicorn-cfg.py apps.backoffice:app'

