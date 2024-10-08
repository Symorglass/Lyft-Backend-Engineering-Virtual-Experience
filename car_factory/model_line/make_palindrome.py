from datetime import datetime

from car import Car
from car_factory.car_factory import carFactory
from engine.engine_type.sternman_engine import SternmanEngine
from battery.battery_type.spinder_battery import spinderBattery

class modelPalindrome(carFactory):
    def __init__(self, warning_light_is_on, current_date, last_service_date) -> None:
        self.warning_light_is_on = warning_light_is_on
        self.current_date = current_date
        self.last_service_date = last_service_date

    def make_model(self):
        engine = SternmanEngine(self.warning_light_is_on)
        battery = spinderBattery(self.current_date, self.last_service_date)
        car = Car(engine, battery)
        return car
