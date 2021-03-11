#!/usr/bin/env python3
# coding:utf-8
from ._base import BaseHandler
from project.project import Proejct
from lib.utils import generate_random
from config import PROJECT_TMP_PATH

from flask import request
import os
import zipfile
import datetime
from shutil import copyfile


class UploadHandler(BaseHandler):
    def save_zip(self, content):
        today = datetime.datetime.now().strftime("%Y%m%d")
        rand = generate_random()[:8]
        name = f'{today}.{rand}.zip'
        path = os.path.abspath(os.path.join(PROJECT_TMP_PATH, name))
        with open(path, "wb") as f:
            f.write(content)
        return name, path

    def decompress_zip(self, zippath):
        fz = zipfile.ZipFile(zippath, 'r')
        dir_path = f"{zippath}.dir"
        for file in fz.namelist():
            fz.extract(file, dir_path)
        fz.close()
        return dir_path

    def move_to_project(self, filepath, project_path):
        copyfile(filepath, project_path)

    def _post(self):
        file = request.files['file']
        filecontent = file.read()

        project_id = self.get_arg("project_id")
        filename = self.get_arg("filename")
        path = self.get_arg("path")

        zipname, zippath = self.save_zip(filecontent)
        zipdir = self.decompress_zip(zippath)
        filepath = os.path.abspath(os.path.join(zipdir, filename))

        _project = Proejct(project_id=project_id)
        _project_path = _project.get_filepath(path)
        _project_filepath = os.path.abspath(os.path.join(_project_path, filename))
        self.move_to_project(filepath, _project_filepath)

        return 1, "success", {}, {}
