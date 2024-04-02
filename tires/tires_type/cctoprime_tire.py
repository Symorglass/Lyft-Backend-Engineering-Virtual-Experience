from tires.tires import Tires

class CctoprimeTire(Tires):
    def __init__(self, tire_wear_sensors_output: list[float]) -> None:
        self.tire_wear_sensors_output = tire_wear_sensors_output

    def tire_need_service(self):
        return sum(self.tire_wear_sensors_output) >= 3.0