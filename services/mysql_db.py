import mysql.connector
from config import Config

def create_db_and_table():

    try:
        conn = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            port=Config.DB_PORT
        )

        cursor = conn.cursor()

        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Config.DB_NAME}")

    except Exception as e:
        print(e,"www")


create_db_and_table()