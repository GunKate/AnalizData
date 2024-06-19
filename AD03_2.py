#Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`.

import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(5)  # массив из 5 случайных чисел
y = np.random.rand(5)

plt.scatter(x, y)
plt.xlabel('ось х')
plt.ylabel('ось y')
plt.title('График рассеяния')

plt.show()