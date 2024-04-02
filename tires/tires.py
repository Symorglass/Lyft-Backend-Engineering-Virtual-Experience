from abc import ABC, abstractmethod

class Tires(ABC):
    @abstractmethod
    def tire_need_service(self):
        pass