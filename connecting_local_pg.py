import psycopg2
import glob
import os


# import sqlite3
# from sqlite3 import OperationalError

# def execute_sql_script(file):
#     fd = open(file, 'r')
#     sqlFile = fd.read()
#     fd.close()

#     sqlCommands = sqlFile.split(';')

#     for command in sqlCommands:
#         try: 
#             c.execute(command)
#         except: OperationalError, msg:
#             print("Command skipped: ", msg)


def create_OC_tables(path, db, user, pw, host, port):
    os.chdir(path)
    with psycopg2.connect(dbname=db, user=user, password=pw, host=host, port=port) as conn:
         with conn.cursor() as curs:
             file = 'Actor.sql'
             SQLQuery = open(file, 'r').read()
             curs.execute(SQLQuery)
             conn.commit()
            # for file in glob.glob("*.sql"):
            #     SQLQuery = open(file, 'r').read()
            #     curs.execute(SQLQuery)
            #     conn.commit()
    conn.close()



if __name__ == "__main__":
    create_OC_tables('..\..\GithubRepos\OpenClimate-Schema\SQL', '', 'postgres', '', '127.0.0.1', '5432')
