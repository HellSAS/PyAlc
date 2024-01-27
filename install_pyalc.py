"""ЭТОТ ФАЙЛ УСТАНОВИТЬ ИЗМЕНЕННУЮ БИБЛИОТЕКУ pyalc В ПАПКУ С БИБЛИОТЕКАМИ PYTHON"""
import sys
import shutil
import os

from _con_message_base import info, error, warning
from _functions_base import *
from colorama import Fore, Back, Style

cls()
print(Fore.GREEN)

pythonLibPath = sys.executable.replace("\\python.exe", "\\Lib\\site-packages\\")
print(pythonLibPath)


source_path = ".\pyalc"
destination_path = pythonLibPath + "\pyalc"

try:
    if os.path.exists(destination_path):
        overwrite = input("The destination folder already exists. Do you want to overwrite it? (y/n): ")
        if overwrite.lower() == "y":
            shutil.rmtree(destination_path)
            shutil.copytree(source_path, destination_path)
            info("Overwrite successful!")
        else:
            info("Installation canceled.")
    else:
        shutil.copytree(source_path, destination_path)
        info("Copy successful!")
except Exception as e:
    error(f"Copy failed: {e}")
