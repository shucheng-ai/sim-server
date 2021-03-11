#!/usr/bin/env python3
# coding:utf-8
from ._base import BaseHandler
from project.project import Proejct
from flask import send_file

import json


class ProejctHandler(BaseHandler):

    def get(self):
        """
        # get project file
        http://127.0.0.1:8000/api/project?project_id=1&type=file&filename=library.json

        # get all project id
        http://127.0.0.1:8000/api/project?type=list
        """
        project_id = self.get_arg("project_id")
        _type = self.get_arg("type")
        filename = self.get_arg("filename")
        _project = None
        if project_id:
            _project = Proejct(project_id)

        if _type == "file":
            filepath = _project.get_filepath(filename)
            attachment_filename = get_attachment_filename(filename)
            return send_file(filepath, attachment_filename=attachment_filename)
        elif _type == "list":
            """
            get all projects
            """
            data = Proejct.get_all()
            return json.dumps({
                "status": 1,
                "data": data
            })
        elif _type == "path":
            path = self.get_arg("path", "/")
            realpath = _project.get_filepath(path)
            data = Proejct.get_path_detail(realpath)
            return json.dumps({
                "status": 1,
                "data": data
            })

    def _post(self):
        """
        type: create_project, file

        1.create project formdata:
        http://127.0.0.1:8000/api/project?type=project&
        {'command':'creat'}

        2.write file
        http://127.0.0.1:8000/api/project?project_id=1&type=file&filename=library.json&
        {filecontent}
        """
        _type = self.get_arg("type")
        project_id = self.get_arg("project_id")
        self.get_formdata()
        res = {}
        if _type == "project":
            command = self.formdata['command']
            if not project_id:
                res = Proejct.run_command(command)
            else:
                params = self.formdata.get("params", [])
                res = Proejct(project_id=project_id).run_project_command(command, params)
        elif _type == "file":
            filename = self.get_arg('filename')
            res["_res"] = Proejct(project_id=project_id).save_file(filename, self.formdata)
            res["filename"] = filename
        return 1, "success", res, {}


def get_attachment_filename(path):
    if not path:
        return ""
    _path = path.split(".")
    if len(_path) <= 2:
        return path
    else:
        return f"{_path[-2]}.{_path[-1]}"
