from AlcoCalc import AlcoCalc, Drinker
from colorama import Fore
from FunctionsBase import *

import art
import os, time

os.system('cls')
print(Fore.GREEN)

def welcomemessage():
    art.tprint("Welcome to AlcoPy", space=True, font="small")
    print("\nIn this program you can calculate your blood alcohol level and intoxication level\n")
    work()

def work():


    def userask():
        UserDict = {}
        UserDict = {a: None for a in Drinker.attributeList}
        userask = ('Enter weight', 'Enter height', 'Enter gender', 'Enter age', 'Enter fullness')
        for a in Drinker.attributeList:
            i = Drinker.attributeList.index(a)
            UserDict[a] = input(f"{userask[i]}: ")
        global User
        User = Drinker(**UserDict)
        #User = Drinker(weight, hight,'gender', age, filness)
        print("\n" + str(User)+ "\n\n\n")


    def askdrinktype():
        print("Choose drink type:\n")
        
        for i in AlcoCalc.drink_types:
            print(f"{i}: {AlcoCalc.drink_types[i]['name']} {AlcoCalc.drink_types[i]['alcohol_content']}%")

        global check
        def askdrinktype1():
            global check
            try:
                check = int(input())
            except:
                askdrinktype1()
        
        try:
            check = int(input("Enter drink type: "))
        except:
            print("Wrong drink type, enter drink type again:")
            askdrinktype1()

        if  check in AlcoCalc.drink_types:
            global drinktype
            drinktype = check
        else:
            print("Wrong drink type, enter drink type again:")
            askdrinktype1()
        global amount
        def askdrinktype2():
            global amount

            try:
                amount = int(input())
            except:
                askdrinktype2()

        try:
            amount = int(input("Enter drink amount: "))
        except:
            print("Wrong drink amount, enter drink amount again:")
            askdrinktype2()

        if amount < 0:
            print("Wrong drink amount, enter drink amount again:")
            askdrinktype2()




    def resultate():
        print("\n\n\n\nYour result:")
        c = AlcoCalc.calculate_alcohol_by_volume(drinktype,amount,User.weight,User.height,User.gender,User.fullness)
        result = AlcoCalc.calculate_alcohol_effect(c)
        for i in result:
            if i == "intoxication_level":
                print(f"{i}: {result[i][1]}")
                print(f"{i}_description: {result[i][2]}")
            else:
                print(f"{i}: {result[i]}")
        time.sleep(5)



    def returntostart():
        print("\n\n\nDo you want to continue? (y/n)")
        check = input()
        if check.lower() == "y":
            cls()
            work()

        else:
            cls()
            exit()


    userask()

    askdrinktype()

    resultate()

    returntostart()


welcomemessage()
