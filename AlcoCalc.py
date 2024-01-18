from FunctionsBase import *

import os 

"""
cfn = check_for_numbers
cfs = check_for_string
cfb = check_for_bool
cfcs = check_for_custom_string

"""
    
class AlcoCalc:
    intoxication_levels = {"sober": 0, "tipsy": 0.5, "drunk": 1, "very drunk": 2, "blackout": 3}
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
        weight = float(weight)
        height = float(height)
        age = int(age)
        fullness = True if fullness.lower() == 'true' else False
        
        self.weight = weight if cfn(weight) else 65
        self.height = height if cfn(height) else 175
        self.gender = gender.lower() if cfcs(['male','female'], gender) else "male"
        self.age = age if cfn(age) else 18
        self.fullness = fullness if cfb(fullness) else True
        
    def __str__(self) -> str:
        string = ""
        for a in self.__dict__:
            string += f"{a} = {self.__dict__[a]}\n"
            
        return string
