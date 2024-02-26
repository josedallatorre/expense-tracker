import psycopg2
import os
from pathlib import Path
from dotenv import load_dotenv

# init from ENV
dotenv_path= Path('../.env')
load_dotenv(dotenv_path=dotenv_path)
HOST = os.getenv('host')
DATABASE = os.getenv('database')
USER= os.getenv('user')
PASSWORD = os.getenv('password')

def connect():
    conn = psycopg2.connect(database = DATABASE, 
                            user = USER, 
                            host= HOST,
                            password = PASSWORD,
                            port = 5432)
    cur = conn.cursor()
    return cur, conn
def insert(cur, conn, t):
    cur.execute("insert into TRANSACTION values(DEFAULT, %s,%s,%s,%s)", t)
    print("Data dynamiccaly Inserted")
    # Make the changes to the database persistent
    conn.commit()

def close(cur, conn):
    # Close cursor and communication with the database
    cur.close()
    conn.close()
