# This is a simple Dockerfile to use while developing
# Docker build for development testing

FROM python:3.8

RUN mkdir /code
WORKDIR /code

COPY requirements.txt setup.py tox.ini ./
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN pip install -e .

COPY core core/
COPY migrations migrations/

EXPOSE 5000
