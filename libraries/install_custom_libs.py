"""ЭТОТ ФАЙЛ УСТАНОВИТЬ ИЗМЕНЕННУЮ БИБЛИОТЕКУ art С ПОДДЕРЖКОЙ ОКРАСА КАЖДОЙ БУКВЫ В СЛОВЕ В ПАПКУ С БИБЛИОТЕКАМИ PYTHON"""
import sys
import shutil
import os

from ConMeassageBase import info, error, warning

pythonLibPath = sys.executable.replace("\\python.exe", "\\Lib\\site-packages\\")
print(pythonLibPath)


source_path = "PyAlc\libraries\color_art"
destination_path = pythonLibPath + "\color_art"

try:
    shutil.copytree(source_path, destination_path)
    info("Copy successful!")
except Exception as e:
    error(f"Copy failed:{e}")
