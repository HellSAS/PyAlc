from AlcoCalc import AlcoCalc, Drinker
from colorama import Fore
from FunctionsBase import *
import os
os.system('cls')
print(Fore.GREEN)
UserDict = {}

UserDict = {a: None for a in Drinker.attributeList}

print(UserDict)
for a in Drinker.attributeList:
    UserDict[a] = input(f"Enter {a}: ")
User = Drinker(**UserDict)
#User = Drinker(60, 169,'male', 17, True)
print("\n" + str(User))

for i in AlcoCalc.drink_types:
    print(f"{i}: {AlcoCalc.drink_types[i]['name']} {AlcoCalc.drink_types[i]['alcohol_content']}%")

def askdrinktype():
    check = int(input("Enter drink type: "))
    if  check in AlcoCalc.drink_types:
        global drinktype
        drinktype = check

    else:
        print("Wrong drink type")
        askdrinktype()
#1919.5242
askdrinktype()
amount = int(input("Enter drink amount: "))




c = AlcoCalc.calculate_alcohol_by_volume(drinktype,amount,User.weight,User.height,User.gender,User.fullness)
result = AlcoCalc.calculate_alcohol_effect(c)
cls()
for i in result:
    if i == "intoxication_level":
        print(f"{i}: {result[i][1]}")
        print(f"{i}_description: {result[i][2]}")
    else:
        print(f"{i}: {result[i]}")
