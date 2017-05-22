FROM python:3.6.1-alpine

MAINTAINER Narunas Krasauskas <narun4sk@gmail.com>

ARG app_path=/opt/rtmbot

COPY app ${app_path}

WORKDIR ${app_path}
RUN pip install -r requirements.txt

CMD ["rtmbot"]
