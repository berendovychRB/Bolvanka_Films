FROM python:3.8

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR app

COPY . .
