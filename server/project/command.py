#!/usr/bin/env python3
# coding:utf-8
import os
from config import CORE_PATH


class Command(object):

    @staticmethod
    def create_project(project_path, import_path=None):
        """
        python3 .../create.py project_root import_from
        """
        command = f"python3 {CORE_PATH}/create.py {project_path}"
        if import_path:
            command = f"python3 {command} {import_path}"
        print(command)
        res = os.system(command)
        return res, command

    @staticmethod
    def run_command(command, project_path, params=[]):
        command = f"python3 {CORE_PATH}/{command}.py {project_path}"
        if params:
            command = f"{command} {' '.join(params)}"
        res = os.system(command)
        return res, command
