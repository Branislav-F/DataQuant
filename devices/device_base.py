from abc import ABC, abstractmethod

class BaseDevice(ABC):
    @abstractmethod
    def connect(self):
        """
        Connectiong to devices
        """
        pass

    @abstractmethod
    def measure(self, quantity: str):
        """
        Measure the specified quantity.
        :param quantity: Name of the quantity (e.g., "current", "voltage").
        :return: The measured value.
        """

    @abstractmethod
    def disconnect(self):
        """
        Disconnect from the device.
        """
        pass


