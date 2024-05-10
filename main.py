import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta
from modules.traffic import generate_traffic


from modules.bandwidth import simulate_bandwidth_usage
from modules.latency import simulate_latency_and_packet_loss
from modules.device_status import monitor_device_status

def simulate_network_activity(duration_hours=1):
    start_time = datetime.now()
    end_time = start_time + timedelta(hours=duration_hours)
    current_time = start_time

    while current_time < end_time:
        # Generar tráfico de red
        traffic_data = generate_traffic()

        # Simular uso de ancho de banda
        bandwidth_data = simulate_bandwidth_usage()

        # Simular latencia y pérdida de paquetes
        latency_data = simulate_latency_and_packet_loss()

        # Monitorear estado de los dispositivos
        device_status_data = monitor_device_status()

        # Guardar o procesar los datos
        print("Traffic Data:", traffic_data)
        print("Bandwidth Data:", bandwidth_data)
        print("Latency Data:", latency_data)
        print("Device Status Data:", device_status_data)

        # Esperar antes de la siguiente simulación (por ejemplo, 1 minuto)
        current_time += timedelta(minutes=1)

if __name__ == "__main__":
    simulate_network_activity(duration_hours=2)  # Simula 2 horas de actividad de red
