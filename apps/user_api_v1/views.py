# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify
from apps.user_api_v1.models import User

user_bp = Blueprint('user_api_v1', __name__)


@user_bp.route('/index')
def user_index():
    """
    test user blueprint
    :return:
    """
    ret_data = {
        "data": "user_bp test",
        "response": "successful",
        "msg": "0"
    }
    return jsonify(ret_data), 200
