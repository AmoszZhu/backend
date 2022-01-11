# -*- coding: utf-8 -*-

"""
init app
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app():
    """
    create app with config file
    :return:
    """
    app = Flask(__name__)
    config_name = os.environ.get('APP_CONFIG')
    app.config.from_object(config_name)

    # use db init app
    db.init_app(app)

    return app
