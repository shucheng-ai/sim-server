#!/usr/bin/env python3
# coding:utf-8
import os

DEBUG = 1
HOST = "0.0.0.0"
PORT = 8000

WEB_SERVER_PATH = os.path.abspath(os.path.dirname(__file__))
SIM_SERVER_PATH = os.path.abspath(os.path.join(WEB_SERVER_PATH, '../'))
WWW_PATH = os.path.abspath(os.path.join(WEB_SERVER_PATH, '../../'))

WEB_STAIC_PATH = os.path.abspath(os.path.join(WWW_PATH, 'sim-web'))
WEB_STAIC_BUILD_PATH = os.path.abspath(os.path.join(WEB_STAIC_PATH, 'dist'))
WEB_INDEX = os.path.abspath(os.path.join(WEB_STAIC_PATH, 'dist', 'index.html'))
WEB_STAIC_COMMON_PATH = os.path.abspath(os.path.join(WEB_STAIC_PATH, 'common'))

# project
PROJECT_PATH = os.path.abspath(os.path.join(WWW_PATH, 'project'))
PROJECT_STORAGE_PATH = os.path.abspath(os.path.join(PROJECT_PATH, 'storage'))
PROJECT_TMP_PATH = os.path.abspath(os.path.join(PROJECT_PATH, 'tmp'))

# core script
CORE_PATH = os.path.abspath(os.path.join(SIM_SERVER_PATH, 'script'))

print(PROJECT_PATH)
print(WEB_INDEX)
