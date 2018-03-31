import psycopg2
import psycopg2.extras
import sys
import os

class ConnectionHelper:

    def __init__(self):
        pg_host = "postgres-container"
        pg_un = "postgres"
        pg_pwd = "postgres"
        pg_db = "postgres"

        if "POSTGRESQL_HOST" in os.environ:
            pg_host = os.environ["POSTGRESQL_HOST"]
        if "POSTGRESQL_USER" in os.environ:
            pg_un = os.environ["POSTGRESQL_USER"]

        if "POSTGRESQL_PASSWORD" in os.environ:
            pg_pwd = os.environ["POSTGRESQL_PASSWORD"]
        if "POSTGRESQL_DATABASE" in os.environ:
            pg_db = os.environ["POSTGRESQL_DATABASE"]

        print("ciao ciao " + pg_un)

        self.host = pg_host
        self.username = pg_un
        self.password = pg_pwd
        self.database = pg_db

    def get_connection(self):
        connection_string = "host='{}' dbname='{}' user='{}' password='{}'".format(self.host, self.database, self.username, self.password)
        return psycopg2.connect(connection_string)

    def execute_query(self, conn, query):
        curs = conn.cursor()
        curs.execute(query)
        conn.commit()
        curs.close()

    def select_query(self, conn, query):
        curs = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        curs.execute(query)
        row_count = 0
        result = ""
        for row in curs:
            row_count += 1
            result += "row: %s    %s \n" % (row_count, row)
        return result
