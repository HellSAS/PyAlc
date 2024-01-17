import os

def cls():
    os.system('cls')
    
    
    
def check_for_numbers(number):
    result = True if number is int or number is float else False
    return result

def cfn(number):
    return check_for_numbers(number)


def check_for_string(string):
    result = True if string is str else False
    return result

def cfs(string):
    return check_for_string(string)


def check_for_bool(boolean):
    result = True if boolean is bool else False
    return result

def cfb(boolean):
    return check_for_bool(boolean)


def check_for_custom_string(args, arg):
    result = True if arg in args else False
    return result

def cfcs(args, arg):
    return check_for_custom_string(args, arg)



