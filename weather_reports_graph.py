import csv
from collections import defaultdict
import matplotlib.pyplot as plt

FILENAME="weather_logs.csv"

def visualize_weather():
    dates=[]
    temps=[]
    conditions=defaultdict(int)

    with open(FILENAME,'r',encoding='utf-8') as f:
        reader=csv.DictReader(f)
        for row in reader:
            try:
                dates.append(row['Date'])
                temps.append(float(row['Temperature']))
                conditions[row['Conditions']]+=1
            except:
                continue
        if not dates:
            print('No data available')
            return
        
    plt.figure(figsize=(12,9))
    plt.plot(dates,temps,marker='o')
    plt.title('Temperature over time')
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.tight_layout()
    plt.grid(True)
    plt.show()

visualize_weather()
