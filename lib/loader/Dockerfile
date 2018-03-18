FROM postgres:latest

ENV DBHOST $DBHOST
ENV DBPORT $DBPORT
ENV DBNAME $DBNAME
ENV DBUSER $DBUSER
ENV DBPASS $DBPASS
ENV DATABASE $DATABASE

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

COPY ./lib/sqlutils /prereqs/sqlutils
WORKDIR /prereqs/sqlutils
RUN python setup.py install

COPY ./database_loader /loader


WORKDIR /loader


CMD bash create_db.sh $DBHOST $DBPORT $DBNAME $DBUSER $DBPASS $DATABASE && python3.6 load_db.py