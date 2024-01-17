import sys
import os
from colorama import Fore
os.system('cls')
print(Fore.GREEN)
class BloodAlcoholCalculator:
    def __init__(self):
        self.drink_types = {
            1: {"name": "beer", "alcohol_content": 0.05},
            2: {"name": "wine", "alcohol_content": 0.12},
            3: {"name": "whiskey", "alcohol_content": 0.4},
            4: {"name": "kvass", "alcohol_content": 0.02},
            5: {"name": "vodka", "alcohol_content": 0.4},
            6: {"name": "champagne", "alcohol_content": 0.12},
            7: {"name": "cognac", "alcohol_content": 0.4},
            8: {"name": "rum", "alcohol_content": 0.4},
            9: {"name": "gin", "alcohol_content": 0.4},
            10: {"name": "tequila", "alcohol_content": 0.4}
        }

    def calculate_blood_alcohol_level(self, drink_number, body_weight, drink_quantity):
        if drink_number not in self.drink_types:
            return "Invalid drink number"

        drink = self.drink_types[drink_number]
        alcohol_content = drink["alcohol_content"]
        blood_alcohol_level = (alcohol_content * drink_quantity * 5.14 * 1.055) / (body_weight * 0.68)
        return blood_alcohol_level

    def get_intoxication_level(self, blood_alcohol_level):
        if blood_alcohol_level < 0.08:
            return "Not intoxicated"
        elif blood_alcohol_level < 0.15:
            return "Mildly intoxicated"
        elif blood_alcohol_level < 0.3:
            return "Significantly intoxicated"
        else:
            return "Dangerously intoxicated"


def main():
    calculator = BloodAlcoholCalculator()
    print("Welcome to AlcoPy, the alcohol calculator!")
    print("Please enter your weight in kilograms: ")
    body_weight = float(input())
    print("Please choose one of the following drinks: ")
    for key, value in calculator.drink_types.items():
        print(f"{key}. {value['name']}")
    drink_number = int(input())
    print("Please enter the number of drinks you had in ml: ")
    drink_quantity = int(input())
    blood_alcohol_level = calculator.calculate_blood_alcohol_level(drink_number, body_weight, drink_quantity)
    intoxication_level = calculator.get_intoxication_level(blood_alcohol_level)
    print(f"Your blood alcohol level is {blood_alcohol_level}")
    print(f"You are {intoxication_level}")
main()