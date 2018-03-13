import psycopg2
import psycopg2.extras
import sys

class ConnectionHelper:

    def __init__(self, host):
        self.host = host

    def get_connection(self):
        connection_string = "host='{}' dbname='postgres' user='postgres' password='postgres'".format(self.host)
        conn = psycopg2.connect(connection_string)
        return conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def execute_query(self, curs, query):
        curs.execute(query)
        row_count = 0
        result = ""
        for row in curs:
            row_count += 1
            result += "row: %s    %s \n" % (row_count, row)
        return result
