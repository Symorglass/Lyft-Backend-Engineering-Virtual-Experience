# from abc import ABC, abstractmethod


# class Car(ABC):
#     def __init__(self, last_service_date):
#         self.last_service_date = last_service_date

#     @abstractmethod
#     def needs_service(self):
#         pass


from Serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery) -> None:
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        if self.engine.engine_need_service() or self.battery.battery_need_service():
            return True
        else:
            return False
