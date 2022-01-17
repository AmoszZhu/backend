# -*- coding: utf-8 -*-

"""
config file
"""


# base config
class BaseConfig:
    SECRET_KEY = '\xbf\xb0\x11\xb1\xcd\xf9\xba\x8bp\x0c...'


# dev config
class DevConfig(BaseConfig):
    DEBUG = False


# test config
class TestConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:zj122900@beacon01.com:3306/beacon?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
