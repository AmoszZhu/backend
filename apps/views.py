# -*- coding: utf-8 -*-

from werkzeug.utils import import_string
from apps import app

blueprint_list = ['apps.user_api_v1:user_bp']
for bp in blueprint_list:
    app.register_blueprint(import_string(bp))
