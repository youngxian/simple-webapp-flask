FROM ubuntu:16.04
RUN apt-get update && apt-get install -y python python-pip && apt-get install -y software-properties-common && add-apt-repository ppa:deadsnakes/ppa && apt-get update
RUN apt-get -y install python3 python3-pip
RUN pip install flask 
RUN pip3 install mysql-connector-python && pip install mysql-connector-python

COPY app.py /opt/
EXPOSE 8080
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080
