from abc import ABC, abstractmethod

class Battery(ABC):
    @abstractmethod
    def battery_need_service(self):
        pass