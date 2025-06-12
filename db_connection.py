import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="edebiyat23",
            database="sports_tracker",
            use_pure=True  # forces pure-python implementation for consistent behavior :contentReference[oaicite:9]{index=9}
        )
        return conn
    except Error as err:
        print("DB connection error:", err)
        return None
