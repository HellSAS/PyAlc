import AlcoClalc

UserDict = {}

for a in AlcoClalc.Drinker.attributeList:
    UserDict[a] = input(f"Enter {a}: ")
    
User = AlcoClalc.Drinker(*UserDict)

print("\n" + str(User))