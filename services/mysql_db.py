import mysql.connector
from config import Config

def create_connection():
    try:
        connection = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            port=Config.DB_PORT
        )
        return connection
    except Exception as e:
        print(e)


def create_db_and_table():

    try:
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Config.DB_NAME};")
        cursor.execute(f"USE {Config.DB_NAME};")

        table_query = """
            CREATE TABLE IF NOT EXISTS weather_data (
                id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                temp FLOAT,
                feels_like FLOAT,
                wind FLOAT,
                timestamp DATETIME NOT NULL,
                humidity INT,
                pressure INT,
                description VARCHAR(255),
                city VARCHAR(255) NOT NULL
            );        
        """

        cursor.execute(table_query)
        print("Tabela i baza utworzone bądź istnieją")
        conn.close()

    except Exception as e:
        print(e)


def save_to_mysql(weather):
    try:
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute(f"USE {Config.DB_NAME};")

        insert_query = """
            INSERT INTO weather_data (
                temp, feels_like, wind, timestamp, humidity, pressure, description, city
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values =(
            weather.get("temp"),
            weather.get("feels_like"),
            weather.get("wind"),
            weather.get("timestamp"),
            weather.get("humidity"),
            weather.get("pressure"),
            weather.get("description"),
            weather.get("city")
        )

        cursor.execute(insert_query, values)
        conn.commit()

        print("Dane pogodowe zostały zapisane do bazy")
        conn.close()

    except Exception as e:
        print(e)