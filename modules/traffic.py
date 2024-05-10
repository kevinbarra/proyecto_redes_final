import csv
from datetime import datetime, timedelta
import random

def generate_traffic(current_time):
    filepath = 'C:\\Users\\kevin\\OneDrive\\Escritorio\\redess\\data\\traffic_data.csv'
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['measurement', 'host', 'traffic_type', 'used_percent', 'time'])
        
        hosts = ['host1', 'host2', 'host3', 'host4']
        traffic_types = ['data', 'voice', 'video']
        for i in range(24):  # Datos cada hora
            timestamp = current_time - timedelta(hours=i)
            for host in hosts:
                traffic_type = random.choice(traffic_types)
                used_percent = round(random.uniform(20, 100), 2)
                writer.writerow(['mem', host, traffic_type, used_percent, timestamp])

    print("Datos de tráfico generados y guardados en CSV con éxito.")

if __name__ == '__main__':
    current_time = datetime.now()
    generate_traffic(current_time)
