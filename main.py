from devices.rigol_dm3068 import RigolDM3068
from storage.influxdb_storage import InfluxDBStorage
import json
from storage.influxdb_storage import InfluxDBStorage

if __name__ == "__main__":
    # Load configuration from config.json
    with open("config.json", "r") as f:
        config = json.load(f)

    storage = InfluxDBStorage(
        url=config["INFLUXDB_URL"],
        token=config["INFLUXDB_TOKEN"],
        org=config["INFLUXDB_ORG"],
        bucket=config["INFLUXDB_BUCKET"]
    )
    # Nájdite všetky pripojené zariadenia
    available_devices = RigolDM3068.find_devices()

    if available_devices:
        # Inicializujte prvé dostupné zariadenie
        resource_name = available_devices[0]
        rigol = RigolDM3068(resource_name)

        try:
            # Pripojte zariadenie
            rigol.connect()

            # Získajte hodnoty napätia a prúdu
            voltage = rigol.measure("voltage")
            current = rigol.measure("current")

            print(f"Voltage: {voltage} V, Current: {current} A")

            # Uložte merania do InfluxDB
            storage.store_measurement("voltage", voltage)
            storage.store_measurement("current", current)

        except Exception as e:
            print(f"Error: {e}")

        finally:
            # Odpojte zariadenie
            rigol.disconnect()
            # Zatvorte spojenie s InfluxDB
            storage.close()
    else:
        print("No devices found.")