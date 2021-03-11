#!/usr/bin/env python3
# coding:utf-8
import os
import json
from config import PROJECT_STORAGE_PATH
from .command import Command


class Proejct(object):
    commands = {
        'create': 'create'
    }

    def __init__(self, project_id):
        self.project_id = project_id
        self.path = os.path.abspath(os.path.join(PROJECT_STORAGE_PATH, f'{project_id}'))

    def create_project(self, import_id=None):
        if import_id:
            import_project = Proejct(project_id=import_id)
            Command.create_project(self.path, import_project.path)
        else:
            Command.create_project(self.path)

    @classmethod
    def create(cls, import_id=None):
        for i in range(1, 9999):
            _project = cls(project_id=i)
            if not _project.is_exist():
                _project.create_project(import_id)
                return {"new_id": i}

    def is_exist(self):
        if not os.path.exists(self.path):
            return False
        else:
            return True

    def get_filepath(self, filename):
        if filename[0] == "/":
            filename = filename[1:]
        path = os.path.abspath(os.path.join(self.path, f'{filename}'))
        return path

    def save_file(self, filename, filecontent):
        _path = self.get_filepath(filename)
        with open(_path, "w") as f:
            f.write(json.dumps(filecontent))
        return _path

    @classmethod
    def run_command(cls, command):
        if command in cls.commands:
            _command = cls.commands[command]
            return getattr(cls, _command)()

    def run_project_command(self, command, params=[]):
        if command in self.commands:
            _command = self.commands[command]
            return getattr(self, _command)()
        else:
            return Command.run_command(command, self.path, params)

    @classmethod
    def get_all(cls):
        return cls.get_path_detail(PROJECT_STORAGE_PATH)

    @classmethod
    def get_path_detail(cls, path):
        def sort_key(e):
            return int(e)

        res, dirs, files = [], [], []
        for _, dirs, files in os.walk(path):
            break

        try:
            dirs.sort(key=sort_key)
        except:
            pass

        for dir in dirs:
            res.append({
                "name": dir,
                "type": "dir",
                "path": os.path.abspath(os.path.join(path, f'{dir}')),
                "filetype": "",
                "filecategory": "",
            })
        for fi in files:
            _file = fi.split(".")
            if len(_file) > 0:
                filetype = _file[-1].lower()
            else:
                filetype = ""
            if filetype in ["jpg", "png", "jpge", "webp"]:
                filetype = "image"
            elif filetype in ["log", "txt"]:
                filetype = "txt"
            res.append({
                "name": fi,
                "type": "file",
                "path": os.path.abspath(os.path.join(path, f'{fi}')),
                "filetype": filetype,
                "filecategory": filetype
            })
        return res
