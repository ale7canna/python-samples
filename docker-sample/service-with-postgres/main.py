#!/bin/python
import time

from my_modules import ConnectionHelper
from flask import Flask

app = Flask(__name__)

@app.route('/')
def method():
    ch = ConnectionHelper("postgres-container")
    cursor = ch.get_connection()
    query = "SELECT 1"
    return ch.execute_query(cursor, query)

@app.route('/hello')
def hello():
    return "hello everyone!"

if __name__ == "__main__":
    print("Hello from sample postgres connection")
    app.run(host="0.0.0.0", debug=True)
