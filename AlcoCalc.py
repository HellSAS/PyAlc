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
    #C=A/(m*r)

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
        24: {"name": "samagon", "alcohol_content": 0.95},


            }



    def сalculate_alcohol_by_volume(drinktype, drink_amount, weight=65, height=175, gender="male", fullness=True) -> float: 
        k = 1 if fullness == False else 10/17
        bmi = weight/((height/100)**2)
        a = drink_amount*AlcoCalc.drink_types[drinktype]["alcohol_content"]*0.789
        rm = 1.0181-0.0113*bmi
        rf = 0.9367-0.01240*bmi
        r = rm if gender == "male" else rf
        bac = a/(weight*r)*k
        result = bac
        return result

    def сalculate_alcohol_effect(c) -> dict:
        can_drive = False
        if c < 0.2:
            can_drive = True
            intoxication_level = "\nsober"
        elif c < 0.59:
            intoxication_level = "\nПоведение:\n*Средневыраженная\n*эйфория\n*РасслаблениеОщущение\n*радости\n*Говорливость\n*Понижение\n*сдержанности\n" + "Нарушения:\n*Концентрация\n"
        elif c < 0.9:
            intoxication_level = "\nПоведение:\n*Притупление ощущения\n*Расторможенность\n*Экстравертность\n" + "Нарушения:\n*Рассуждение\n*Глубина восприятия\n*Периферическое зрение\n*Приспособление зрачка к свету\n" 
        elif c < 1.9:
            intoxication_level = "\nПоведение:\n*Сверх-экспрессивность\n*Переменчивость эмоций\n*Гнев или печаль\n*Неистовость\n*Снижение либидо\n" + "Нарушения:\n*Рефлексы\n*Время реакции\n*Основные моторные навыки\n*Способность к контролю движения (появляется шатающаяся походка)\n*Нечленораздельная речь\n*Эрекция (у мужчин, временно)\n*Вероятность временного алкогольного отравления\n"
        elif c < 2.9:
            intoxication_level = "\nПоведение:\n*Ступор\n*Потеря способности к пониманию\n*Ослабление способностей к ощущению\n" +"Нарушения:\n*Вероятность потери сознания\n*Тяжелое нарушение моторики\n*Потеря памяти" 
        elif c < 3.9:
            intoxication_level = "\nПоведение:\n*Сильное угнетение функций центральной нервной системы\n*Потеря сознания\n*Вероятность смерти\n" + "Нарушеняи:\n*Контроль над мочеиспусканием\n*Дыхание\n*чувство равновесия (полная утрата)\n*Сердцебиение\n"
        elif c < 5:
            intoxication_level = "\nПоведение:\n*Полная утрата контроля за поведением\n*Потеря сознания\n*Вероятность смерти\n" + "Нарушения:\n*Дыхание\n*Сердцебиение\n*Контроль над движением зрачков (Нистагм)\n"
        else:
            intoxication_level = "\nПоведение:\n*Высокий риск отравления\n*Высокий риск смерти"
        time_to_sober_hours = c*60/0.15/60

        result = {"promiles": c, "intoxication_level": intoxication_level, "time_to_sober_minutes": time_to_sober_hours, "can_drive": can_drive}
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
