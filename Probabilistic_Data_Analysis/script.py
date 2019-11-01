import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Считывание данных
titanic_data = pd.read_csv('train.csv')
ages = titanic_data.Age

# Подсчет параметров и их вывод
param = []
param.append(ages.mean())
param.append(ages.var())
param.append(ages.median())
param.append(ages.mode()[0])

param_names = [ 'Mean (Yellow)', 'Variance', 'Median (Blue)', 'Mode (Green)' ]

for i in range(len(param)):
    print(param_names[i] + ' =', param[i], end='\n \n')

# Проверка на выбросы
Q3 = ages.quantile(0.75)
Q1 = ages.quantile(0.25)
IQR = Q3 - Q1
interval = [Q1 - 1.5 * IQR, Q3 + 3 * IQR]

# Отрисовка гистограммы, параметров и диапазона проверки на выбросы
ages.hist()
# plt.axhline(y=0.5, color='r', linestyle='-')

plt.axvline(x=param[0], color='y', linestyle='-')
plt.axvline(x=param[2], color='b', linestyle='-.')
plt.axvline(x=param[3], color='g', linestyle='--')
plt.axvline(x=interval[0], color='r', linestyle='-')
plt.axvline(x=interval[1], color='r', linestyle='-')
plt.show()