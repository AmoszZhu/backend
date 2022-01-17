FROM python:3.10.1
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
ENV APP_PORT=59003 APP_HOST=0.0.0.0 APP_CONFIG="apps.config.TestConfig" FLASK_APP=manage.py
CMD ["python", "manage.py"]