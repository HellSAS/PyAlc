from _functions_base import *
from accessify import private, protected


"""
tpi = tryParseInt
tpf = tryParseFloat

cfn = check_for_numbers
cfs = check_for_string
cfb = check_for_bool
cfcs = check_for_custom_string

"""
     
class AlcoCalc:


    ## Словарь с данными об уровнях опьянения.
    intoxication_levels = {
        "sober": [0.2, "sober", "Sober"],
        "slightly drunk": [0.59, "slightly drunk", "\nBehavior:\n*Moderate euphoria\n*Relaxation\n*Feeling of joy\n*Talkativeness\n*Decreased inhibition\n" + "Impairments:\n*Concentration"],
        "mild intoxication": [0.9, "mild intoxication", "\nBehavior:\n*Sensory dulling\n*Extraversion\n" + "Impairments:\n*Reasoning\n*Depth perception\n*Peripheral vision\n*Pupil adaptation to light"],
        "moderate intoxication": [1.9, "moderate intoxication", "\nBehavior:\n*Hyper-expressiveness\n*Emotional variability\n*Anger or sadness\n*Aggression\n*Decreased libido\n" + "Impairments:\n*Reflexes\n*Reaction time\n*Basic motor skills\n*Ability to control movement (staggering gait)\n*Slurred speech\n*Erection (temporary, in males)\n*Increased risk of alcohol poisoning"],
        "severe intoxication": [2.9, "severe intoxication", "\nBehavior:\n*Stupor\n*Loss of comprehension\n*Diminished sensory abilities\n" + "Impairments:\n*Likelihood of loss of consciousness\n*Severe motor impairment\n*Memory loss"],
        "extremely severe poisoning": [5.0, "extremely severe poisoning", "\nBehavior:\n*Complete loss of behavioral control\n*Loss of consciousness\n*Risk of death\n" + "Impairments:\n*Breathing\n*Heart rate\n*Control of eye movements (Nystagmus)"],
        "high risk of death": [float("inf"), "high risk of death", "\nBehavior:\n*Coma\n" + "Impairments:\n*Failure of all sensory organs"],
    }

    ## Словарь с данными о типах напитков.
    """    drink_types = {
        
        1: {"name": "beer", "alcohol_content": 0.05},
        2: {"name": "wine", "alcohol_content": 0.12},
        3: {"name": "whiskey", "alcohol_content": 0.4},
        4: {"name": "kvass", "alcohol_content": 0.002},
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
        24: {"name": "samagon", "alcohol_content": 0.95},
     }"""
    
    def calculate_alcohol_by_volume(alcohol_content, drink_amount, weight, height, gender, fullness) -> float: 
        """! Рассчитывает уровень алкоголя в крови [грамм спирта/литр крови].
        @param drink_type   Тип напитка.
        @param drink_amount   Количество выпитого напитка (в миллилитрах).
        @param weight   Вес человека (в килограммах).
        @param height   Рост человека (в сантиметрах).
        @param gender   Пол человека.
        @param fullness   Уровень сытости человека.
        @return  [грамм.спирта/литр.крови].
        """

        alcohol_content = alcohol_content/100
        if alcohol_content < 0:
            alcohol_content = -alcohol_content
        k = 1 if fullness == False else 10/17
        bmi = weight/((height/100)**2)
        a = drink_amount*alcohol_content*0.789
        rm = 1.0181-0.0113*bmi
        rf = 0.9367-0.01240*bmi
        r = rm if gender == "male" else rf
        bac = a/(weight*r)*k
        result = bac
        return result

    def calculate_alcohol_effect(c) -> dict: 
        """! Рассчитывает уровень опьянения.
        @param c   Уровень алкоголя в крови [грамм.спирта/литр.крови].
        @return  {"promiles": float, "intoxication_level": str, "time_to_sober_hours": float, "can_drive": bool}
        """
        
        can_drive = True
        
        if c > AlcoCalc.intoxication_levels["sober"][0]:
                can_drive = False
                
        for i in AlcoCalc.intoxication_levels:
            if c < AlcoCalc.intoxication_levels[i][0]:
                intoxication_level = AlcoCalc.intoxication_levels[i]
                break
            else:
                intoxication_level = AlcoCalc.intoxication_levels["high risk of death"]
                can_drive = False
        time_to_sober_hours = c/0.15 # 0.15грамм/ч - среднее время выведения алкоголя из организма

        result = {"promiles": c, "intoxication_level": intoxication_level, "time_to_sober_hours": time_to_sober_hours, "can_drive": can_drive}
        return result
class Drinker:
    attributeList = ["weight", "height", "gender", "age", "fullness"]
    
    def __init__(self, weight=65, height=175, gender="male", age=18, fullness=True):
        """! Конструктор класса Drinker.
        @param weight   Вес человека (в килограммах).
        @param height   Рост человека (в сантиметрах).
        @param gender   Пол человека.
        @param age   Возраст человека.
        @param fullness   Уровень сытости человека.
        """
        
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
        """! Возвращает строку с данными о человеке.
        @return Строка с данными о человеке.
        """
        
        string = ""
        for a in self.__dict__:
            string += f"{a} = {self.__dict__[a]}\n"
            
        return string
