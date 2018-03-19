FROM python:latest

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY . /prereqs
WORKDIR /prereqs
RUN python setup.py install
RUN rm -rf /prereqs

COPY ./main.py /usr/local/manager/main.py
WORKDIR /usr/local/manager

ENV LANG_FILENAME ''
ENV DICT_PATH ''
ENV LIST_PATH ''

RUN mkdir -p /tmp/structure/output/dict/reflections
RUN mkdir -p /tmp/structure/output/dict/categories

CMD python3.6 main.py