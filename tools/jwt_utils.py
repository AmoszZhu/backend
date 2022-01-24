# -*- coding: utf-8 -*-

"""
1. jwt组成
    header,payload,signature
    a. header 头部
"""

# from flask import current_app
import jwt


def generate_jwt(payload, expire, sercet=None):
    """

    :param payload: dict 载荷
    :param expire: datetime 过期时间
    :param sercet: 密钥
    :return:
    """
    _payload = {
        'exp': expire
    }
    _payload.update(payload)

    # if not sercet:
    #     secret = current_app.config['JWT_SECRET']

    token = jwt.jwk_from_dict(_payload, sercet, algorithms='HS256')
    print(token)


generate_jwt({"name": "zhu jian"}, expire=300)
