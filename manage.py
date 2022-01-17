# -*- coding: utf-8 -*-

from apps import create_app, db
from flask import jsonify
from flask_migrate import Migrate
import os

# create app
app = create_app()

migrate = Migrate(app, db)


@app.route('/')
def hello_world():
    ret_data = {
        "data": "hello world",
        "response": "successful",
        "msg": "0"
    }
    return jsonify(ret_data), 200


if __name__ == '__main__':
    app_host = os.environ.get("APP_HOST", "0.0.0.0")
    app_port = os.environ.get("APP_PORT", 59003)
    app.run(host=app_host, port=app_port)
