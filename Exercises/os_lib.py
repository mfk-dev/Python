import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Wassup?") # We printed "Wassup?" but it wont show up because we cleared the terminal right after that.
clear()
