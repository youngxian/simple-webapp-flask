FROM ubuntu:16.04
RUN apt-get update && apt-get install -y python python-pip && apt-get install -y software-properties-common && add-apt-repository ppa:deadsnakes/ppa && apt-get update
RUN apt-get -y install python3 && pip install --upgrade pip
RUN pip install flask && pip3 install mysql-connector-python
COPY app.py /opt/
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080
