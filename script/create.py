# !/usr/bin/env python3
# coding:utf-8
import os
import sys
from shutil import copyfile

path = sys.argv[1]
_path = os.path.abspath(os.path.dirname(__file__))
library = os.path.abspath(os.path.join(_path, 'library.json'))

if not os.path.exists(path):
    os.makedirs(path)
    copyfile(library, f'{path}/library.json')