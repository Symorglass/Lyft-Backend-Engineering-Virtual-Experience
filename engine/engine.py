from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def engine_need_service(self):
        pass