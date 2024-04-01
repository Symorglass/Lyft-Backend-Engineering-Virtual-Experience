# from datetime import datetime

# from engine.capulet_engine import CapuletEngine


# class Thovex(CapuletEngine):
#     def needs_service(self):
#         service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
#         if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
#             return True
#         else:
#             return FalseS




from datetime import datetime

from car import Car
from car_factory.car_factory import carFactory
from engine.engine_type.capulet_engine import CapuletEngine
from battery.battery_type.nubbin_battery import nubbinBattery

class modelCalliope(carFactory):
    def __init__(self, current_mileage, last_service_mileage, current_date, last_service_date) -> None:
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.current_date = current_date
        self.last_service_date = last_service_date

    def make_model(self):
        engine = CapuletEngine(self.current_mileage, self.last_service_mileage)
        battery = nubbinBattery(self.current_date, self.last_service_date)
        car = Car(engine, battery)
        return car