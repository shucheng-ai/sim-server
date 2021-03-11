#!/usr/bin/env python3
# coding:utf-8
from app import app
from config import DEBUG, HOST, PORT

print(f"app run debug:{DEBUG};host:{HOST},{PORT};debug:{DEBUG}")

app.run(
    debug=DEBUG,
    host=HOST,
    port=PORT
)
