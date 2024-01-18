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
    #C=A/(m*r)
    class Drink_types:
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
                10: {"name": "tequila", "alcohol_content": 0.4},
                11: {"name": "absinthe", "alcohol_content": 0.7},
                12: {"name": "sambuca", "alcohol_content": 0.4},
                13: {"name": "martini", "alcohol_content": 0.15},
                14: {"name": "vermouth", "alcohol_content": 0.18},
                15: {"name": "campari", "alcohol_content": 0.25},
                16: {"name": "jagermeister", "alcohol_content": 0.35},
                17: {"name": "absolut", "alcohol_content": 0.4},
                18: {"name": "jack daniels", "alcohol_content": 0.4},
                19: {"name": "jim beam", "alcohol_content": 0.4},
                20: {"name": "bacardi", "alcohol_content": 0.4},
                21: {"name": "malibu", "alcohol_content": 0.21},
                22: {"name": "baileys", "alcohol_content": 0.17},
                23: {"name": "sambuca", "alcohol_content": 0.4},
                24: {"name": "sambuca", "alcohol_content": 0.4},

            }


    """ def сalculate_alcohol_by_volume(drink_types, a, drink_amount, weight=65, height=175, gender="male", fullness=True) -> float:
        vm = 2.447 + 0.3362*weight + 10.74*height
        vf = 2.097 + 0.2466 * weight + 10.69 * height
        p = 0.51 if fullness else 0.55
        if gender == 'male':
            vm = 2.447 + 0.3362*weight + 10.74*height
            c = ((drink_types[a]["alcohol_content"])*drink_amount*p)/vm
        else:
            vf = 2.097 + 0.2466 * weight + 10.69 * height
            c = ((drink_types[a]["alcohol_content"])*drink_amount*p)/vf
        result = c
        return result"""
    def сalculate_alcohol_by_volume(drinktype, drink_amount, weight=65, height=175, gender="male", fullness=True) -> float:
        vm = 2.447 + 0.3362*weight + 10.74*height
        vf = 2.097 + 0.2466 * weight + 10.69 * height
        p = 0.51 if fullness else 0.55
        if gender == 'male':
            vm = 2.447 + 0.3362*weight + 10.74*height
            c = (AlcoCalc.Drink_types.drink_types[drinktype]["alcohol_content"]*drink_amount*p)/vm
        else:
            vf = 2.097 + 0.2466 * weight + 10.69 * height
            c = (AlcoCalc.Drink_types.drink_types[drinktype]["alcohol_content"]*drink_amount*p)/vf
        result = c
        return result

    def сalculate_alcohol_effect(c) -> dict:
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
