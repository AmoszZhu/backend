# -*- coding: utf-8 -*-

from flask_restplus import Resource, Namespace, fields
from flask import request, jsonify
from apps.user_api_v1.models import User
from apps import db
from apps.user_api_v1.user_params import *

# 定义 user namespace for swagger
user_ns = Namespace('user_api_v1', description='Api of user')


@user_ns.route('/register')
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
    @user_ns.response(model=create_user_success, code=201, description="create user success")
    @user_ns.response(model=create_user_fail, code=400, description="create user failed")
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
            return {
                       "data": None,
                       "response": "failed",
                       "msg": "Lack of parameter"
                   }, 400

        if password != password2:
            return {
                       "data": None,
                       "response": "failed",
                       "msg": "password2 != password"
                   }, 400

        try:
            user_list = User.query.filter_by(phoneNumber=phone).all()
            print(f"user_list: {user_list}")
        except Exception as e:
            print(e)
            return {
                       "data": None,
                       "response": "failed",
                       "msg": "Database exception"
                   }, 400

        if user_list:
            return {
                "data": None,
                "response": "failed",
                "msg": "The phone has been registered"
            }

        user = User(userName=username, phoneNumber=phone, passWord=password)
        print(f"new user info; {user}")
        try:
            db.session.add(user)
            db.session.commit()
            return {
                       "data": {
                           "uid": user.id
                       },
                       "response": "successful",
                       "msg": "0"
                   }, 201
        except Exception as e:
            print(e)
            return {
                       "data": None,
                       "response": "failed",
                       "msg": "Add user fail"
                   }, 400


@user_ns.route('/login')
class UserLogin(Resource):
    # param
    user_login_param = user_ns.model('user_login_param', user_login_param)

    # response
    user_token = user_ns.model('user_token', user_token)
    user_login_success = user_ns.model('user_login_success',{
        "data": fields.Nested(user_token),
        "response": fields.String(description="Result status of the request"),
        "msg": fields.String("error msg")
    })
    user_login_fail = user_ns.model('user_login_fail', {
        "data": fields.String(),
        "response": fields.String(description="Result status of the request"),
        "msg": fields.String("error msg")
    })

    @user_ns.doc(body=user_login_param)
    @user_ns.response(model=user_login_success, description="user login successful", code=200)
    @user_ns.response(model=user_login_fail, description="user login failed", code=400)
    def post(self):
        """
        user login
        :return:
        """
        # get username and pwd from body
        request_body = request.json
        if not request_body:
            return {
                       "data": None,
                       "response": "failed",
                       "msg": "Lack of body"
                   }, 200

        # verify params
        username = request_body.get("username", None)
        password = request_body.get("password", None)
        if not all([username, password]):
            return {
                       "data": None,
                       "response": "failed",
                       "msg": "Lack of parameter"
                   }, 400

        try:
            user_list = User.query.filter_by(userName=username).all()
            print(f"user {user_list} login")
        except Exception as e:
            print(e)
            return {
                       "data": None,
                       "response": "failed",
                       "msg": "Database exception"
                   }, 400
        if not user_list:
            return {
                       "data": None,
                       "response": "failed",
                       "msg": "User does not exist, please register first"
                   }, 400

        user = user_list[0]

        # verify password
        if password != user.passWord:
            return {
                       "data": None,
                       "response": "failed",
                       "msg": "Password is wrong, please try again"
                   }, 400

        print(user)
