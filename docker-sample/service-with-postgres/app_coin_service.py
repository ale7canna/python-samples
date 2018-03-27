#!/bin/python
import time
import sys
import os

from shared.coin_service import CoinService
from shared.my_modules import ConnectionHelper

_connection = ConnectionHelper()
_coin_service = CoinService()

def coin_service():
    while True:
        try:
            coin_method()
        except:
            print("Unexpected error:", sys.exc_info()[0])
        time.sleep(59)

def coin_method():
    res = _coin_service.get_change()
    query = "INSERT INTO change_value (ts, value_cambia_valute, value_xe, value_diff, value_diff_perc) VALUES ('%s', %f, %f, %f, %f)" % (res[0], res[1], res[2], res[3], res[4])
    conn = _connection.get_connection()
    _connection.execute_query(conn, query)

if __name__ == "__main__":
    print("service starting...")
    coin_service()
