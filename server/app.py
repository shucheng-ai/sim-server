# !/usr/bin/env python3
# coding:utf-8
from flask import Flask, send_from_directory
from config import WEB_STAIC_BUILD_PATH, PROJECT_PATH, PROJECT_STORAGE_PATH, PROJECT_TMP_PATH, WEB_STAIC_COMMON_PATH, \
    WEB_INDEX
from urls import init_urls
from lib.utils import mkdir, cleandir

mkdir(PROJECT_PATH)
mkdir(PROJECT_STORAGE_PATH)
cleandir(PROJECT_TMP_PATH)
mkdir(PROJECT_TMP_PATH)

app = Flask(
    __name__,
    static_url_path="/static",
    static_folder=WEB_STAIC_BUILD_PATH,
    template_folder=WEB_STAIC_BUILD_PATH
)


@app.route('/')
@app.route('/index')
@app.route('/project')
@app.route('/demo')
@app.route('/project/<project_id>')
@app.route('/project/<project_id>/<title>')
def index(project_id=None, title=None):
    with open(WEB_INDEX, "r") as f:
        text = f.read()
        return text

init_urls(app)
