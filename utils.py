import argparse

def get_parser():
    # set the argument parser
    parser = argparse.ArgumentParser(description="Car service application")
    parser.add_argument("model_name", type=str, help="Name of the car model")
    parser.add_argument("--current_mileage", type=int, required=False, default=0, help='Current mileage of the car')
    parser.add_argument("--last_service_mileage", type=int, required=False, default=0, help='Mileage in the last service')
    parser.add_argument("--warning_light_is_on", action='store_true', required=False, help='Is the warning light on')
    parser.add_argument("--current_date", type=str, required=True, default='2024-01-01', help='Current date')
    parser.add_argument("--last_service_date", type=str, required=True, default='2024-01-01', help='Date of the last service')
    return parser