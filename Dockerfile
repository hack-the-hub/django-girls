FROM        python:3

MAINTAINER  django@tyndyll.net

ENV         PYTHONUNBUFFERED 1

ADD         . /volman
WORKDIR     /volman
RUN         pip install -r requirements.txt


