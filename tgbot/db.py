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
                            # Open a cursor to perform database operations
    cur = conn.cursor()
    # Execute a command: create datacamp_courses table
    cur.execute("""CREATE TABLE datacamp_courses(
                course_id SERIAL PRIMARY KEY,
                course_name VARCHAR (50) UNIQUE NOT NULL,
                course_instructor VARCHAR (100) NOT NULL,
                topic VARCHAR (20) NOT NULL);
                """)
    # Make the changes to the database persistent
    conn.commit()
    # Close cursor and communication with the database
    cur.close()
    conn.close()

connect()
print('done')