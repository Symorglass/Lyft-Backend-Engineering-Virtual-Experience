from tires.tires import Tires

class CarriganTire(Tires):
    def __init__(self, tire_wear_sensors_output: list[float]) -> None:
        self.tire_wear_sensors_output = tire_wear_sensors_output

    def tire_need_service(self):
        for tire in self.tire_wear_sensors_output:
            if tire >= 0.9:
                return True
        return False