#!/bin/python
from my_modules import ConnectionHelper

def main():
    ch = ConnectionHelper()
    cursor = ch.get_connection()
    query = "SELECT 1"
    ch.execute_query(cursor, query)

if __name__ == "__main__":
    print("Hello from sample postgres connection")
    main()
