#!/bin/python
import time
import sys
import os
import requests

from coin_service import CoinService

_coin_service = CoinService()

def coin_service():
    endpoint = 'http://application:5000/add'
    if "SERVICE_ENDPOINT" in os.environ:
        endpoint = os.environ['SERVICE_ENDPOINT']
    iterations = 0
    while True:
        try:
            iterations += 1
            print("iteration number %i" % iterations)
            coin_method(endpoint)
        except:
            print("Unexpected error:", sys.exc_info()[0])
        time.sleep(59)

def coin_method(url):
    res = _coin_service.get_change()
    query = "INSERT INTO change_value (ts, value_cambia_valute, value_xe, value_diff, value_diff_perc) VALUES ('%s', %f, %f, %f, %f)" % (res[0], res[1], res[2], res[3], res[4])
    rx = requests.post(url, data= {'querytoadd':query})
 
if __name__ == "__main__":
    print("service starting...")
    coin_service()
