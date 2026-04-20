from services.openweather_api import get_weather
from services.excel_files import save_to_excel, read_excel
from services.dashboard import render_dashboard
from services.mysql_db import create_db_and_table, save_to_mysql, get_all_weather
import time

create_db_and_table()

# results_excel = read_excel("weather_data.xlsx")
# results_sql = get_all_weather()
# for r in results_sql:
#     print(r)

while True:
    weather = get_weather()
    save_to_excel([weather])
    save_to_mysql(weather)
    print("Pobieram i zapisuję dane")
    time.sleep(5)

# render_dashboard("lisbon.xlsx")
