# -*- coding: utf-8 -*-

"""
init app
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

db = SQLAlchemy()


def create_app():
    """
    create app with config file
    :return:
    """
    app = Flask(__name__)
    config_name = os.environ.get('APP_CONFIG', "apps.config.TestConfig")
    app.config.from_object(config_name)

    # use db init app
    db.init_app(app)

    CORS(app)

    return app
