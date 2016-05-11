FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN apt-get -qq update
RUN apt-get -qq install unixodbc unixodbc-dev freetds-dev freetds-bin tdsodbc
ADD odbc.ini /etc/odbc.ini
ADD odbcinst.ini /etc/odbcinst.ini
ADD freetds.conf /etc/freetds/freetds.conf

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/