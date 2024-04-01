from abc import ABC, abstractmethod

class carFactory(ABC):
    @abstractmethod
    def make_model(self):
        pass
