# -*- coding: utf-8 -*-

"""
定义 user的参数
"""
from flask_restplus import fields

create_user_param = {
    "username": fields.String(required=True, description='username'),
    "password": fields.String(required=True, description='password'),
    "password2": fields.String(required=True),
    "phone": fields.String(required=True)
}

create_user_data = {
    "uid": fields.Integer(description="user id")
}