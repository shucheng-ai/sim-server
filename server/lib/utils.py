#!/usr/bin/env python3
# coding:utf-8
import os
import time
import random
from hashlib import md5
from shutil import rmtree


def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def cleandir(path):
    if os.path.exists(path):
        rmtree(path)


def generate_random(sstr=None):
    ti = int(time.time())
    if not sstr:
        string = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        random.shuffle(string)
        sstr = ''.join(string)
    rand = str(random.randint(0, 99999))
    res = str(ti) + sstr + rand
    res = res.encode("utf-8")
    res = md5(res).hexdigest()
    return res


def generate_md5(data):
    data = f"{data}"
    data = data.encode("utf-8")
    data = md5(data).hexdigest()
    return data
