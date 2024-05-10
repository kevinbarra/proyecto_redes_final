import csv
import random
from datetime import datetime

def simulate_bandwidth_usage(current_time):
    bandwidth_file = 'C:\\Users\\kevin\\OneDrive\\Escritorio\\redess\\data\\bandwidth_usage.csv'
    with open(bandwidth_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['device', 'bandwidth_usage_in_mbps', 'bandwidth_usage_out_mbps', 'max_bandwidth_mbps', 'time'])
        
        for i in range(10):
            usage_in = random.uniform(0, 100)
            usage_out = random.uniform(0, 100)
            max_bandwidth = random.uniform(100, 1000)
            writer.writerow([f"device_{i}", usage_in, usage_out, max_bandwidth, current_time])

    print("Datos de ancho de banda generados y guardados en CSV con éxito.")

if __name__ == "__main__":
    current_time = datetime.now()
    simulate_bandwidth_usage(current_time)
