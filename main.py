from services.openweather_api import get_weather
from services.excel_files import save_to_excel, read_excel
from services.dashboard import render_dashboard
from services.mysql_db import create_db_and_table, save_to_mysql
import time

create_db_and_table()

while True:
    weather = get_weather()
    save_to_excel([weather])
    save_to_mysql(weather)
    print("Pobieram i zapisuję dane")
    time.sleep(5)


result = read_excel("weather_data.xlsx")

# render_dashboard("lisbon.xlsx")


# git add .
# git commit -m 'wiadmosc'
# git push

# git push -u origin nazwa_galezi