import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_db_username",
        password="your_db_password",
        database="your_db_name"
    )
