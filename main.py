import argparse
from car_factory.model_line.make_calliope import modelCalliope
from car_factory.model_line.make_glissade import modelGlissade
from car_factory.model_line.make_palindrome import modelPalindrome
from car_factory.model_line.make_rorschach import modelRorschach
from car_factory.model_line.make_thovex import modelThovex


class Application(object):
    def __init__(self):
        # Declaration
        self.model = None
        self.model_name = None
        self.current_mileage = None
        self.last_service_mileage = None
        self.current_date = None
        self.last_service_date = None
        self.warning_light_is_on = None

    def initialize(self):
        # Simulating reading in car model selection argument
        if self.model_name == "Calliope":
            self.model = modelCalliope(self.current_mileage, self.last_service_mileage, self.current_date, self.last_service_date)
        elif self.model_name == "Glissade":
            self.model = modelGlissade(self.current_mileage, self.last_service_mileage, self.current_date, self.last_service_date)
        elif self.model_name == "Palindrome":
            self.model = modelPalindrome(self.warning_light_is_on, self.current_date, self.last_service_date)
        elif self.model_name == "Rorschach":
            self.model = modelGlissade(self.current_mileage, self.last_service_mileage, self.current_date, self.last_service_date)
        elif self.model_name == "Thovex":
            self.model = modelGlissade(self.current_mileage, self.last_service_mileage, self.current_date, self.last_service_date)
        else:
            raise Exception("Error! Unknown Model Type.")

    def main(self, model_name, current_mileage, last_service_mileage, warning_light_is_on, current_date, last_service_date):
        # parse in argument
        self.model_name = model_name
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.warning_light_is_on = warning_light_is_on

        # initialization
        self.initialize()
        car = self.model.make_model()
        need_service = car.needs_service()
        print(f"Does the car need service? {'Yes' if need_service else 'No'}")


# Example usage
if __name__ == '__main__':
    # set up the argument parser
    parser = argparse.ArgumentParser(description="Car service application")
    parser.add_argument("model_name", type=str, help="Name of the car model")
    parser.add_argument("--current_mileage", type=int, required=False, default=0, help='Current mileage of the car')
    parser.add_argument("--last_service_mileage", type=int, required=False, default=0, help='Mileage in the last service')
    parser.add_argument("--warning_light_is_on", action='store_true', required=False, help='Is the warning light on')
    parser.add_argument("--current_date", type=str, required=True, default='2024-01-01', help='Current date')
    parser.add_argument("--last_service_date", type=str, required=True, default='2024-01-01', help='Date of the last service')

    args = parser.parse_args()
    app = Application()
    app.main(args.model_name, 
             args.current_mileage, 
             args.last_service_mileage, 
             args.warning_light_is_on, 
             args.current_date, 
             args.last_service_date)


# Example use cases
# python3 main.py Calliope --current_mileage 10000 --last_service_mileage 8000 --current_date 03-01-2022 --last_service_date 01-01-2024
# python3 main.py Palindrome --warning_light_is_on --current_date 2022-03-01 --last_service_date 2022-01-01