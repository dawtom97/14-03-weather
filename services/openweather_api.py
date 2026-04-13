import requests
from datetime import datetime
from common.tools import kelvin_to_celsius, ms_to_km

def get_weather(city):

    API_KEY = "abaf891f881f0013ba7df3fa450461b0" # Nie powinien być na widoku!

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        record = {
            "city": data.get("name"),
            "temp": kelvin_to_celsius(data.get("main").get("temp")),
            "feels_like": kelvin_to_celsius(data.get("main").get("feels_like")),
            "wind": ms_to_km(data.get("wind").get("speed")),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "humidity": data.get("main").get("humidity"),
            "pressure": data.get("main").get("pressure"),
            "description": data.get("weather")[0].get("description")
        }

        return record
    except Exception as e:
        print(e)






