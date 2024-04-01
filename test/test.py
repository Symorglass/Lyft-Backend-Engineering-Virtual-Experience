import unittest
from datetime import datetime

from car_factory.model_line.make_calliope import modelCalliope
from car_factory.model_line.make_glissade import modelGlissade
from car_factory.model_line.make_palindrome import modelPalindrome
from car_factory.model_line.make_rorschach import modelRorschach
from car_factory.model_line.make_thovex import modelThovex


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        model = modelCalliope(current_mileage, last_service_mileage, today, last_service_date)
        car = model.make_model()
        self.assertTrue(car.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        model = modelCalliope(current_mileage, last_service_mileage, today, last_service_date)
        car = model.make_model()
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 30001
        last_service_mileage = 0

        model = modelCalliope(current_mileage, last_service_mileage, today, last_service_date)
        car = model.make_model()
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 30000
        last_service_mileage = 0

        model = modelCalliope(current_mileage, last_service_mileage, today, last_service_date)
        car = model.make_model()
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        model = modelGlissade(current_mileage, last_service_mileage, today, last_service_date)
        car = model.make_model()
        self.assertTrue(car.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        model = modelGlissade(current_mileage, last_service_mileage, today, last_service_date)
        car = model.make_model()
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 60001
        last_service_mileage = 0

        model = modelGlissade(current_mileage, last_service_mileage, today, last_service_date)
        car = model.make_model()
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 60000
        last_service_mileage = 0

        model = modelGlissade(current_mileage, last_service_mileage, today, last_service_date)
        car = model.make_model()
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        model = modelPalindrome(warning_light_is_on, today, last_service_date)
        car = model.make_model()
        self.assertTrue(car.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False

        model = modelPalindrome(warning_light_is_on, today, last_service_date)
        car = model.make_model()
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = True

        model = modelPalindrome(warning_light_is_on, today, last_service_date)
        car = model.make_model()
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False

        model = modelPalindrome(warning_light_is_on, today, last_service_date)
        car = model.make_model()
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        model = modelRorschach(current_mileage, last_service_mileage, today, last_service_date)
        car = model.make_model()
        self.assertTrue(car.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        model = modelRorschach(current_mileage, last_service_mileage, today, last_service_date)
        car = model.make_model()
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 60001
        last_service_mileage = 0

        model = modelRorschach(current_mileage, last_service_mileage, today, last_service_date)
        car = model.make_model()
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 60000
        last_service_mileage = 0

        model = modelRorschach(current_mileage, last_service_mileage, today, last_service_date)
        car = model.make_model()
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        model = modelThovex(current_mileage, last_service_mileage, today, last_service_date)
        car = model.make_model()
        self.assertTrue(car.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        model = modelThovex(current_mileage, last_service_mileage, today, last_service_date)
        car = model.make_model()
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 30001
        last_service_mileage = 0

        model = modelThovex(current_mileage, last_service_mileage, today, last_service_date)
        car = model.make_model()
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 30000
        last_service_mileage = 0

        model = modelThovex(current_mileage, last_service_mileage, today, last_service_date)
        car = model.make_model()
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()

# To test: 
# Navigate to the root of project.
# Run the module using the following command:
# python3 -m test.test