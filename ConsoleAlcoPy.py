from AlcoCalc import AlcoCalc, Drinker

UserDict = {}

UserDict = {a: None for a in Drinker.attributeList}

print(UserDict)
for a in Drinker.attributeList:
    UserDict[a] = input(f"Enter {a}: ")
#def сalculate_alcohol_by_volume(drinktype, drink_amount, weight=65, height=175, gender="male", fullness=True) -> float:
User = Drinker(**UserDict)
print("\n" + str(User))
for i in AlcoCalc.Drink_types.drink_types:
    print(f"{i}: {AlcoCalc.Drink_types.drink_types[i]['name']}")
def askdrinktype():
    check = int(input("Enter drink type: "))
    if  check in AlcoCalc.Drink_types.drink_types:
        global drinktype
        drinktype = check

    else:
        print("Wrong drink type")
        askdrinktype()

askdrinktype()
amount = int(input("Enter drink amount: "))




c = AlcoCalc.сalculate_alcohol_by_volume(drinktype,amount,User.weight,User.height,User.gender,User.fullness)
print(c)