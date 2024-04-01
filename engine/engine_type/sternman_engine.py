from engine.engine import Engine

class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on) -> None:
        self.warning_light_is_on = warning_light_is_on

    def engine_need_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False