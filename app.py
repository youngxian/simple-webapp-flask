from mysql.connector import (connection)
import os
from flask import Flask
import mysql.connector
from mysql.connector import errorcode

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'


@app.route("/", methods=['GET', 'POST'])
def main():

    try:
        cnx = mysql.connector.connect(
            user='scott', password='password', host='127.0.0.1', database='employees')
        print ("Database connected")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
       

    return "Welcome!"


@app.route('/how are you')
def hello():
    return 'I am good, how about you?'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

