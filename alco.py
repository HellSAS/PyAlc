# Dictionary of known drinks and their alcohol content in grams per milliliter

"""drinks = {
    "beer": 0.05,
    "wine": 0.12,
    "vodka": 0.4,
    # Add more drinks and their alcohol content here
}"""

#def calculate_blood_alcohol_level(drink, weight, volume):


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


# Example usage
weight = float(input("Введите ваш вес в килограммах: "))
drink = input("Введите название напитка: ")
volume = float(input("Введите объем напитка в миллилитрах: "))

blood_alcohol_level = calculate_blood_alcohol_level(drink, weight, volume)
print(f"Blood alcohol level: {blood_alcohol_level:.2f}")
