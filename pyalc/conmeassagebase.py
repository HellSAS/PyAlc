
from colorama import Fore, Back, Style

def error(message):
    print(Fore.RED + Style.BRIGHT + "[ERROR] " + Style.DIM + message + Style.RESET_ALL)
    
def info(message):
    print(Fore.BLUE + Style.BRIGHT + "[INFO] " + Style.DIM + message + Style.RESET_ALL)
    
def warning(message):
    print(Fore.YELLOW + Style.BRIGHT + "[WARNING] " + Style.DIM  + message + Style.RESET_ALL)
    
if __name__ == "__main__":
    print("\n")
    error("This is an error message.\n\n")
    info("This is an info message.\n\n")
    warning("This is a warning message.")
    input("\n\nPress Enter to exit...")