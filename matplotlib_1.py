import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('ggplot')

x = []
y = []

while True:
    number = int(input("Enter the numbers that you want the square of: ( Enter 0 to stop)"))
    square = number ** 2

    if number == 0:
        break
    else:
        x.append(number)
        y.append(square)

fig, ax = plt.subplots()
ax.plot(x, y, marker='o', linestyle='-', color='blue')
ax.set_xlabel('Number')
ax.set_ylabel('Square of Number')
ax.set_title('Square of Numbers')
plt.show()
