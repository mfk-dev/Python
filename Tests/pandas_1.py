import pandas as pd

people = [{
    "Name": "MFK", 
    "age": 23, 
    "login_date": "2026-02-24"
}, {
    "Name": "Nicco", 
    "age": 25, 
    "login_date": "2026-02-24"
}, {
    "Name": "Nietzsche", 
    "age": 19, 
    "login_date": "2026-02-24"
}]

df = pd.DataFrame(people)

print("---"*10)
print(df.head())
print("---"*10)
print(f"Sum of ages: {df['age'].sum()}")
print("---"*10)
print(f"Average age: {df['age'].mean()}")
print("---"*10)
print(f"Person with highest age: {df.nlargest(1, 'age')}")
print("---"*10)
