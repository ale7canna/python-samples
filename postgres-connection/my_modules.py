import psycopg2
import psycopg2.extras
import sys

class ConnectionHelper:

    def get_connection(self):
        connection_string = "host='pg' dbname='postgres' user='postgres' password='postgres'"
        conn = psycopg2.connect(connection_string)
        return conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def execute_query(self, curs, query):
        curs.execute(query)
        row_count = 0
        for row in curs:
            row_count += 1
            print("row: %s    %s " % (row_count, row))
