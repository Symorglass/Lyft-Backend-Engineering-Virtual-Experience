from battery.battery import Battery

class nubbinBattery(Battery):
    def __init__(self, current_date, last_service_date) -> None:
        self.current_date = current_date
        self.last_service_date = last_service_date
    
    def battery_need_service(self):
        last_serviced = self.last_service_date
        date_which_battery_should_be_serviced_by = last_serviced.replace(year=last_serviced.year + 4)
        if date_which_battery_should_be_serviced_by < self.current_date:
            return True
        else:
            return False
    