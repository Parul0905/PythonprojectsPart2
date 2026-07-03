import os
import csv
from datetime import datetime
import requests

FILENAME = 'weather_logs.csv'
API_KEY = 'b1e93dbbb33db8df35b20c4807a4d921'
# keys are usually hidden inside a .env file

if not os.path.exists(FILENAME):
    with open(FILENAME, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'Temperature', 'City', 'Condition'])


def log_weather():
    city = input('Enter the city: ').strip()
    if not city:
        print('City name cannot be empty.')
        return

    date = datetime.now().strftime('%Y-%m-%d')
    with open(FILENAME, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('Date') == date and row.get('City', '').lower() == city.lower():
                print('Entry for this city and date already exists.')
                return

    url = (
        f'http://api.openweathermap.org/data/2.5/weather'
        f'?q={city}&appid={API_KEY}&units=metric'
    )

    try:
        response = requests.get(url, timeout=10)
    except requests.RequestException as exc:
        print('Could not reach the weather API:', exc)
        return

    if response.status_code != 200:
        print('API ERROR:', response.status_code)
        return

    data = response.json()
    temp = data['main']['temp']
    condition = data['weather'][0]['main']

    with open(FILENAME, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([date, temp, city, condition])

    print('Weather entry logged successfully.')


if __name__ == '__main__':
    log_weather()

