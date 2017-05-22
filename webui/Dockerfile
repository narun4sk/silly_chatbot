FROM python:3.6.1-alpine

MAINTAINER Narunas Krasauskas <narun4sk@gmail.com>

ARG app_path=/opt/webui

COPY ./app ${app_path}

WORKDIR ${app_path}
RUN pip install -r requirements.txt

CMD ["python3", "run.py"]
