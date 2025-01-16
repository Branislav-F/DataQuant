import pyvisa
from device_base import BaseDevice

class RigolDM3068(BaseDevice):
    def __init__(self, resource_name):
        self.resource_name = resource_name
        self.rm = pyvisa.ResourceManager()
        self.device = None

    def connect(self):
        """
        Connect to the Rigol DM3068 device.
        """
        self.device = self.rm.open_resource(self.resource_name)
        self.device.timeout = 5000
        print(f"Connected to {self.resource_name}")

    def measure(self, quantity: str):
        """
        Measure the specified quantity.
        :param quantity: Name of the quantity (e.g., "current", "voltage").
        :return: The measured value.
        """
        commands = {
            "current": ":MEAS:CURR:DC?",
            "voltage": ":MEAS:VOLT:DC?",
        }

        if quantity not in commands:
            raise ValueError(f"Unsupported quantity: {quantity}")

        result = self.device.query(commands[quantity])
        print(f"Measured {quantity}: {result.strip()}")
        return float(result)

    def disconnect(self):
        """
        Disconnect from the Rigol DM3068 device.
        """
        if self.device:
            self.device.close()
            self.device = None
            print(f"Disconnected from {self.resource_name}")

    @staticmethod
    def find_devices():
        """
        Find all connected VISA devices.
        :return: List of available device addresses.
        """
        rm = pyvisa.ResourceManager()
        devices = rm.list_resources()
        print("Available devices:")
        for device in devices:
            print(f" - {device}")
        return devices

# Example Usage
if __name__ == "__main__":
    # Find all connected devices
    available_devices = RigolDM3068.find_devices()

    if available_devices:
        # Initialize the first found device
        resource_name = available_devices[0]
        rigol = RigolDM3068(resource_name)

        try:
            # Connect to the device
            rigol.connect()

            # Measure voltage and current
            voltage = rigol.measure("voltage")
            current = rigol.measure("current")

            print(f"Voltage: {voltage} V, Current: {current} A")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            # Disconnect the device
            rigol.disconnect()
    else:
        print("No devices found.")
