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

plt.plot(x, y, label='y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = x^2')
plt.show()
