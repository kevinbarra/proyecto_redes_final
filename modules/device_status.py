import csv
import random
from datetime import datetime, timedelta

def monitor_device_status(current_time):
    filepath = 'C:\\Users\\kevin\\OneDrive\\Escritorio\\redess\\data\\device_status.csv'
    locations = ['Data Center 1', 'Data Center 2', 'Office', 'Remote Site']
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['device', 'status', 'location', 'last_operative', 'failure_rate', 'time'])
        
        for i in range(10):
            status = random.choice(['operativo', 'inactivo', 'fallando'])
            location = random.choice(locations)
            last_operative = current_time - timedelta(hours=random.randint(1, 72))
            failure_rate = random.uniform(0, 0.5) if status == 'fallando' else 0
            writer.writerow([
                f"device_{i}",
                status,
                location,
                last_operative.strftime('%Y-%m-%d %H:%M:%S'),
                failure_rate,
                current_time.strftime('%Y-%m-%d %H:%M:%S')
            ])

    print("Estado de los dispositivos monitorizados y datos guardados en CSV con éxito.")

if __name__ == "__main__":
    current_time = datetime.now()
    monitor_device_status(current_time)
