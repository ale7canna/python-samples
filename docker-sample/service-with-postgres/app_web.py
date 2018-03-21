#!/bin/python
import time

from my_modules import ConnectionHelper
from coin_service import CoinService
from flask import Flask

app = Flask(__name__)
_connection = ConnectionHelper("postgres-container")
_coin_service = CoinService()

@app.route('/')
def method():
    conn = _connection.get_connection()
    query = "SELECT * FROM change_value"
    return _connection.select_query(conn, query)

@app.route('/hello')
def hello():
    return "hello everyone!"

@app.route('/coin')
def coin():
    res = _coin_service.get_change()
    line = "values: %s, %f, %f, %f, %f" % (res[0], res[1], res[2], res[3], res[4])
    return line

if __name__ == "__main__":
    app.run()

