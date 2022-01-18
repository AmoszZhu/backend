# -*- coding: utf-8 -*-

from flask import jsonify, json, request
from apps.user_api_v1 import user_bp
from apps.user_api_v1.models import User


@user_bp.route('/index')
def test_user():
    return "test user"
