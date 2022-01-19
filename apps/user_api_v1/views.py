# -*- coding: utf-8 -*-

from flask_restplus import Resource, Namespace, fields
from flask import request, jsonify
from apps.user_api_v1.models import User
from apps.user_api_v1.user_params import create_user_param, create_user_data

# 定义 user namespace for swagger
user_ns = Namespace('user_api_v1', description='Api of user')


@user_ns.route('/user')
class UserApi(Resource):
    create_user_param = user_ns.model('create_user_param', create_user_param)
    create_user_data = user_ns.model('create_user_data', create_user_data)
    create_user_success = user_ns.model('create_user_success', {
        "data": fields.Nested(create_user_data),
        "response": fields.String(description="Result status of the request"),
        "msg": fields.String("error msg")
    })
    create_user_fail = user_ns.model('create_user_fail', {
        "data": fields.String(),
        "response": fields.String(description="Result status of the request"),
        "msg": fields.String("error msg")
    })

    @user_ns.doc(body=create_user_param)
    @user_ns.marshal_with(create_user_success, code=201)
    @user_ns.marshal_with(create_user_fail, code=200)
    def post(self):
        """
        create user
        :return:
        """

        request_body = request.json
        if not request_body:
            return {
                "data": None,
                "response": "failed",
                "msg": "Lack of body"
            }, 200
        username = request_body.get("username", None)
        password = request_body.get("password", None)
        password2 = request_body.get("password2", None)
        phone = request_body.get("phone", None)

        # verify params
        if not all([username, password, password2, phone]):
            return jsonify({
                "data": None,
                "response": "failed",
                "msg": "Lack of parameter"
            }), 200
