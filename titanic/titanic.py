# Импортируем библиотеку pandas для работы с данными
# Импортируем библиотеку matplotlib для построения графиков
# Для удобства код лучше запускать в jupiter notebook

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('titanic.csv')

print(df.head())
print("avg df =",df.mean()[6])
print(df.sum()[5])
print(df.describe(include=['object']))

print(df['Age'].mean(), df['Age'].median())
print(df.groupby('Sex')['Age'].describe())




df['Age'].plot(kind='hist', bins=10)
plt.ylabel("Columns")
plt.xlabel("Age")
plt.show()
