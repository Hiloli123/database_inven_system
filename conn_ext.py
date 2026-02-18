import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
from contextlib import contextmanager

@contextmanager

def db_connection():
    try:
        conn = psycopg2.connect(database=os.getenv("DB_NAME"),
                            user=os.getenv('DB_USER'),
                            password=os.getenv('DB_PASS'),
                            host=os.getenv('DB_HOST'),
                            port=os.getenv('DB_PORT'))
    
        yield conn
        
    except Exception as e:
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
    
    



    