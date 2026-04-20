import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    API_KEY = os.getenv("API_KEY")
    API_CITY= os.getenv("API_CITY")
    EXCEL_PATH = "weather_data.xlsx"
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
