from AlcoCalc import AlcoCalc, Drinker
from colorama import Fore, Style
from FunctionsBase import *

import color_art as art
import os, time
import sys


cls()
print(Fore.GREEN)

w = ""
color = (Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.RED)
text_start = f"Welcome     to     AlcoPy"
#space=True, font="small"

    
def welcomemessage():
    art.tprint(text_start, colors = color)

    print(Fore.GREEN +"\nIn this program you can calculate your blood alcohol level and intoxication level\n")
    work()

def work():

    def userask():
        UserDict = {}
        UserDict = {a: None for a in Drinker.attributeList}
        userask = (Fore.CYAN + 'Enter weight(kg)' + Style.RESET_ALL, 
                   Fore.CYAN + 'Enter height(cm)' + Style.RESET_ALL, 
                   Fore.CYAN + 'Enter gender(male/female)' + Style.RESET_ALL, 
                   Fore.CYAN + 'Enter age(not necessary)' + Style.RESET_ALL, 
                   Fore.CYAN + 'Enter fullness(true/false)' + Style.RESET_ALL)
        for a in Drinker.attributeList:
            i = Drinker.attributeList.index(a)
            UserDict[a] = input(f"{userask[i]}: ")
        global User
        User = Drinker(**UserDict)
        print("\n" + str(User) + "\n\n\n")

    def askdrinktype():
        """print(Fore.BLUE + "Choose drink type:\n" + Style.RESET_ALL)
        
        for i in AlcoCalc.drink_types:
            print(f"{Fore.YELLOW}{i}{Style.RESET_ALL}: {AlcoCalc.drink_types[i]['name']} {AlcoCalc.drink_types[i]['alcohol_content']}%")

        global check
        def askdrinktype1():
            global check
            try:
                check = int(input())
            except:
                askdrinktype1()
        
        try:
            check = int(input(Fore.CYAN + "\n\nEnter drink type(num of drink type): " + Style.RESET_ALL))
        except:
            print(Fore.RED + "Wrong drink type, enter drink type again:" + Style.RESET_ALL)
            askdrinktype1()

        if  check in AlcoCalc.drink_types:
            global drinktype
            drinktype = check
        else:
            print(Fore.RED + "Wrong drink type, enter drink type again:" + Style.RESET_ALL)
            askdrinktype1()"""
        global alcohol_content
        def askdrinktype1():
            global alcohol_content
            try:
                alcohol_content = float(input())
            except:
                askdrinktype1()
        try:
            print(Fore.BLUE + f"write the amount of alcohol in the drink:{Fore.CYAN}\nwrite in the format x(%) - number of percents:\n\n" + Style.RESET_ALL)
            alcohol_content = float(input())
        except:
            print(Fore.RED + "Wrong alcohol content, enter alcohol content again:" + Style.RESET_ALL)
            askdrinktype1()
        global amount
        def askdrinktype2():
            global amount

            try:
                amount = float(input())
            except:
                askdrinktype2()

        try:
            amount = float(input(Fore.CYAN + "\n\nEnter drink amount: " + Style.RESET_ALL))
        except:
            print(Fore.RED + "Wrong drink amount, enter drink amount again:" + Style.RESET_ALL)
            askdrinktype2()

        if amount < 0:
            print(Fore.RED + "Wrong drink amount, enter drink amount again:" + Style.RESET_ALL)
            askdrinktype2()

    def resultate():
        print(Fore.BLUE + "\n\n\n\nYour result:" + Style.RESET_ALL)
        c = AlcoCalc.calculate_alcohol_by_volume(alcohol_content, amount, User.weight, User.height, User.gender, User.fullness)
        result = AlcoCalc.calculate_alcohol_effect(c)
        for i in result:
            if i == "intoxication_level":
                print(f"{Fore.BLUE}{i}{Style.RESET_ALL}: {Fore.RED}{result[i][1].replace('*', Fore.RED + '*' + Style.RESET_ALL)}{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{i}_description:{Style.RESET_ALL}{result[i][2].replace('*', Fore.RED + '*' + Style.RESET_ALL)}{Style.RESET_ALL}")
            else:
                print(f"{Fore.BLUE}{i}:{Style.RESET_ALL} {result[i]}{Style.RESET_ALL}" if isinstance(result[i], str) else f"{Fore.BLUE}{i}: {Fore.WHITE}{result[i]}{Style.RESET_ALL}")
        time.sleep(5)


    def returntostart():
        print(Fore.GREEN+"\n\n\nDo you want to continue? (y/n)")
        check = input()
        if check.lower() == "y":
            os.system('cls')
            work()
        else:
            os.system('cls')
            exit()

    userask()
    askdrinktype()
    resultate()
    returntostart()

welcomemessage()
