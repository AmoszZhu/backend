FROM python:3.10.1

WORKDIR /backend
ADD . /backend
RUN pip install -r requirements.txt