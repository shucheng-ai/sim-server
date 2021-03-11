#!/usr/bin/env python3
# coding:utf-8
import json
from flask.views import MethodView
from flask import make_response, request


class BaseHandler(MethodView):
    formdata = {}

    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__()

    def get_arg(self, k, default=None):
        return request.args.get(k, default)

    def get_formdata(self):
        try:
            self.formdata = request.get_json()
        except:
            self.formdata = {}

    def json_response(self, status=0, msg='', data={}, **kwargs):
        data = {
            'status': status,
            'msg': msg,
            'data': data
        }
        data.update(kwargs)
        data = json.dumps(data)
        resp = make_response(data)
        resp.headers['Content-Type'] = 'application/json'
        resp.headers['Access-Control-Allow-Headers'] = 'origin, x-csrftoken, content-type, accept'
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Max-Age'] = 1678000
        return resp

    def _get(self):
        return 0, '', {}, {}

    def get(self):
        staus, msg, data, kwargs = self._get()
        return self.json_response(staus, msg, data, **kwargs)

    def _post(self):
        return 0, '', {}, {}

    def post(self):
        staus, msg, data, kwargs = self._post()
        return self.json_response(staus, msg, data, **kwargs)

    def _put(self):
        return 0, '', {}, {}

    def put(self):
        staus, msg, data, kwargs = self._put()
        return self.json_response(staus, msg, data, **kwargs)

    def _delete(self):
        return 0, '', {}, {}

    def delete(self):
        staus, msg, data, kwargs = self._delete()
        return self.json_response(staus, msg, data, **kwargs)
