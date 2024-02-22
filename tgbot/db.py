import psycopg2
import os
from pathlib import Path
from dotenv import load_dotenv
dotenv_path= Path('../.env')
load_dotenv(dotenv_path=dotenv_path)
HOST = os.getenv('host')
DATABASE = os.getenv('database')
USER= os.getenv('user')
PASSWORD = os.getenv('password')
print(HOST, DATABASE, USER, PASSWORD)
def connect():
    conn = psycopg2.connect(database = DATABASE, 
                            user = USER, 
                            host= HOST,
                            password = PASSWORD,
                            port = 5432)
    cur = conn.cursor()
    cur.execute("INSERT INTO \"CLIENT\"(username) VALUES ('jose');")
    print("Data Inserted")
    # Make the changes to the database persistent
    conn.commit()
    # Close cursor and communication with the database
    cur.close()
    conn.close()
    print('created table with psy ')

connect()