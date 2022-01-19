FROM python:3.8.10

WORKDIR /backend
ADD . /backend
RUN pip install -r requirements.txt