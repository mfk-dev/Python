import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

name = input("Enter the student name: ")
clear()

math = int(input("Enter the mathematics score: "))
clear()

chemistry = int(input("Enter the chemistry score: "))
clear()

physics = int(input("Enter the physics score: "))
clear()

biology = int(input("Enter the biology score: "))
clear()

average = (math + chemistry + physics + biology) / 4

print("---" * 10)
print(f"Mathematics Score: {math}")
print(f"Chemistry Score: {chemistry}")
print(f"Physics Score: {physics}")
print(f"Biology Score: {biology}")
print("---" * 10)

if average == 100:
    print(f"{name} has an {average} average score of numerical subjects and is awarded a perfect score!")
elif average >= 90:
    print(f"{name} has an {average} average score of numerical subjects and is awarded an A grade!")
elif average >= 80:
    print(f"{name} has an {average} average score of numerical subjects and is awarded a B grade!")
elif average >= 70:
    print(f"{name} has an {average} average score of numerical subjects and is awarded a C grade!")
elif average >= 60:
    print(f"{name} has an {average} average score of numerical subjects and is awarded a D grade!")
else:
    print(f"{name} has an {average} average score of numerical subjects and is awarded an F grade! Better luck next time.")
