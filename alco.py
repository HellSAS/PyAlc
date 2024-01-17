# Dictionary of known drinks and their alcohol content in grams per milliliter
drinks = {
    "beer": 0.05,
    "wine": 0.12,
    "vodka": 0.4,
    # Add more drinks and their alcohol content here
}

def calculate_blood_alcohol_level(drink, weight, volume):
    # Calculate the total amount of alcohol in grams
    alcohol = volume * drinks[drink]
    # Calculate the blood alcohol level
    blood_alcohol_level = alcohol / (weight * 0.7)
    return blood_alcohol_level

# Example usage
weight = float(input("Введите ваш вес в килограммах: "))
drink = input("Введите название напитка: ")
volume = float(input("Введите объем напитка в миллилитрах: "))

blood_alcohol_level = calculate_blood_alcohol_level(drink, weight, volume)
print(f"Blood alcohol level: {blood_alcohol_level:.2f}")
