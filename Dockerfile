FROM python:3.8.10

WORKDIR /backend
ADD . /backend
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt