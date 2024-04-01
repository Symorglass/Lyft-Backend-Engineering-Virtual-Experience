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
