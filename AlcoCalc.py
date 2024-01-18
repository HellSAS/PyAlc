from FunctionsBase import *

import os 

"""
tpi = tryParseInt
tpf = tryParseFloat

cfn = check_for_numbers
cfs = check_for_string
cfb = check_for_bool
cfcs = check_for_custom_string

"""
    
class AlcoCalc:
    intoxication_levels = {"sober": 0, "tipsy": 0.5, "drunk": 1, "very drunk": 2, "blackout": 3}
    
    drink_types = {
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
    
    def сalculate_alcohol_by_volume(alcohol_strength, drink_amount, weight=65, height=175, gender="male", age=18, fullness=True) -> float:
        pass # Your code here
        
        result = float
        return result
    
    def сalculate_alcohol_effect(alcohol_strength, drink_amount, weight=65, height=175, gender="male", age=18, fullness=True) -> dict:
        pass # Your code here
        
        result = {"promiles": float, "intoxication_level": str, "time_to_sober_minutes": int, "can_drive": bool}
        return result
    
class Drinker:
    attributeList = ["weight", "height", "gender", "age", "fullness"]
    
    def __init__(self, weight=65, height=175, gender="male", age=18, fullness=True):
        weight = float(weight) if tpf(weight) and cfn(float(weight)) else 65
        gender = gender.lower() if cfcs(['male','female'], gender) else "male"
        height = float(height) if tpf(height) and cfn(float(height)) else 175
        age = int(age) if tpi(age) and cfn(int(age)) else 18
        if type(fullness) is not bool:
            fullness = True if tps(fullness) and fullness.lower() == 'true' else False
        
        self.weight = weight
        self.height = height 
        self.gender = gender
        self.age = age 
        self.fullness = fullness 
        
    def __str__(self) -> str:
        string = ""
        for a in self.__dict__:
            string += f"{a} = {self.__dict__[a]}\n"
            
        return string
