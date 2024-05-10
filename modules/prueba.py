from influxdb_client_3 import InfluxDBClient3, Point
import time

token = "3Ic67O_8_Sr1FVSiHZN2s2A_V9mxznhqXbE5eCDwg4aflO5zUFI5F7YVb0ezfgwwBAwjBr5iTc_TAAbGreGp4w=="
org = "redes"
bucket = "networkmetrics"
host = "https://us-east-1-1.aws.cloud2.influxdata.com"

client = InfluxDBClient3(url=host, token=token, org=org)

data = [
    {"location": "Klamath", "species": "bees", "count": 23},
    {"location": "Portland", "species": "ants", "count": 30},
    {"location": "Klamath", "species": "bees", "count": 28},
    {"location": "Portland", "species": "ants", "count": 32},
    {"location": "Klamath", "species": "bees", "count": 29},
    {"location": "Portland", "species": "ants", "count": 40},
]

for entry in data:
    point = (
        Point("census")
        .tag("location", entry["location"])
        .field(entry["species"], entry["count"])
    )
    client.write(bucket=bucket, record=point)
    time.sleep(1)

print("Datos escritos con éxito en InfluxDB.")
