FROM python:3.8.10

WORKDIR /backend
ADD . /backend
RUN apt-get update &&\
    apt-get install -y vim
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt