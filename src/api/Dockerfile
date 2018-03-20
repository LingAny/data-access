FROM python:latest

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY ./lib/sqlutils /prereqs/sqlutils
WORKDIR /prereqs/sqlutils
RUN python setup.py install

COPY ./lib/apiutils /prereqs/apiutils
WORKDIR /prereqs/apiutils
RUN python setup.py install

COPY ./lib/netutils /prereqs/netutils
WORKDIR /prereqs/netutils
RUN python setup.py install

RUN rm -rf /prereqs

COPY . /api
WORKDIR /api
RUN python setup.py install
RUN rm -rf /api

COPY ./main.py /usr/local/ling_any/main.py
WORKDIR /usr/local/ling_any

ENV CACHE_TYPE simple
ENV DB_NAME lingany
ENV DB_USER lingany
ENV DB_PASS lingany
ENV DB_SERVICE postgres
ENV DB_PORT 5432
ENV SERVER_NAME lingany
ENV DB_HOST postgres
ENV WEB_PORT 80

CMD /usr/local/bin/gunicorn -w 1 -b :$WEB_PORT main:app