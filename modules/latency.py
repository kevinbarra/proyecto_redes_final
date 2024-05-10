import csv
import numpy as np
from datetime import datetime, timedelta

def simulate_latency_and_packet_loss(current_time):
    filepath = 'C:\\Users\\kevin\\OneDrive\\Escritorio\\redess\\data\\latency_packet_loss.csv'
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['node_pair', 'response_time_ms', 'packet_loss_percent', 'time'])
        
        # Simulación de latencia y pérdida de paquetes entre pares de nodos
        for i in range(10):
            timestamp = current_time - timedelta(hours=i)
            for j in range(3):
                node_pair = f"node_{j}_to_node_{(j+1)%3}"
                response_time = np.random.normal(loc=100, scale=30)
                packet_loss = np.random.uniform(0, 5)
                writer.writerow([node_pair, response_time, packet_loss, timestamp])

    print("Datos de latencia y pérdida de paquetes generados y guardados en CSV con éxito.")

if __name__ == "__main__":
    current_time = datetime.now()
    simulate_latency_and_packet_loss(current_time)
