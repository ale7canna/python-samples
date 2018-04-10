#!/bin/python
import time

from my_modules import ConnectionHelper
from flask import Flask
from flask import request 

app = Flask(__name__)

_connection = ConnectionHelper()

@app.route('/add', methods=['POST'])
def add_method():
    content = request.form.get('querytoadd')
    conn = _connection.get_connection()
    _connection.execute_query(conn, content)
    return 'OK'

@app.route('/')
def method():
    conn = _connection.get_connection()
    query = "SELECT * FROM change_value ORDER BY id DESC"
    return _connection.select_query(conn, query)

@app.route('/hello')
def hello():
    return "hello everyone!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
