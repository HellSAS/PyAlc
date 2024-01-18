from AlcoCalc import AlcoCalc, Drinker
from colorama import Fore
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




c = AlcoCalc.сalculate_alcohol_by_volume(drinktype,amount,User.weight,User.height,User.gender,User.fullness)
result = AlcoCalc.сalculate_alcohol_effect(c)
for i in result:
    print(f"{i}: {result[i]}")

