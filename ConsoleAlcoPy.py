from AlcoCalc import AlcoCalc, Drinker

UserDict = {}

UserDict = {a: None for a in Drinker.attributeList}
    
print(UserDict)
for a in Drinker.attributeList:
    UserDict[a] = input(f"Enter {a}: ")

User = Drinker(**UserDict)

print("\n" + str(User))

print(AlcoCalc.сalculate_alcohol_by_volume(40, 100))