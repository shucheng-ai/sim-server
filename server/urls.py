#!/usr/bin/env python3
# coding:utf-8
from api.project import ProejctHandler
from api.upload import UploadHandler

urls_list = [
    ['/api/project', ProejctHandler],
    ['/api/upload', UploadHandler],
]


def init_urls(app, urls=urls_list):
    count = 0
    for item in urls:
        count += 1
        try:
            name = "router-{}".format(count)
            app.add_url_rule(item[0], view_func=item[1].as_view(name))
        except Exception as e:
            print(e)
