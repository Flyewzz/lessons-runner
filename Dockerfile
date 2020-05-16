FROM python:2.7

RUN apt-get update && apt-get install -y \
    xvfb

RUN pip install -r requirements.txt

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1

ENV APP_HOME /usr/src/app
WORKDIR /$APP_HOME
COPY . $APP_HOME/

ENTRYPOINT [ "python", "./main.py" ]