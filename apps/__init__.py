# -*- coding: utf-8 -*-

"""
init app
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restplus import Api
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


# create app
app = create_app()

# 使用数据库迁移
migrate = Migrate(app, db)

# swagger api
api = Api(app, version='1.0', title='User Api',
          description="The api of user")

from apps import views
