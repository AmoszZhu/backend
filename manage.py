# -*- coding: utf-8 -*-

import os
from apps import app


if __name__ == '__main__':
    app_host = os.environ.get("APP_HOST", "0.0.0.0")
    app_port = os.environ.get("APP_PORT", 59003)
    app.run(host=app_host, port=app_port)
