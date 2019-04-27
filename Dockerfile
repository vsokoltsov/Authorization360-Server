FROM python:3.7.2

RUN mkdir /authorization360
WORKDIR /authorization360

ADD . /authorization360

RUN pip install -r requirements.txt
