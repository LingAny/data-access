FROM python:latest

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY . /api
WORKDIR /api
RUN python setup.py install
RUN rm -rf /api

COPY ./main.py /usr/local/ling_any/main.py
WORKDIR /usr/local/ling_any

ENV CACHE_TYPE simple
ENV WEB_PORT 80

CMD /usr/local/bin/gunicorn -w 4 -b :$WEB_PORT main:app