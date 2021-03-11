#!/usr/bin/env python3
# coding:utf-8
from ._base import BaseHandler

EXPORT_HANDLERS = []


class IndexHandler(BaseHandler):
    name = 'index_handler'
    api = '/api/index'

    def get(self):
        return self.json_response(data={})


EXPORT_HANDLERS.append(IndexHandler)
