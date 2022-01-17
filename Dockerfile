FROM python:3.10.1

RUN apt-get update && apt-get install -y \
        gcc \
        libsasl2-dev \
        libldap2-dev \
        libssl-dev \
        gettext \
        vim \
        zip \
        xmlsec1 \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

WORKDIR /backend
ADD . /backend
RUN pip install -r requirements.txt