import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Corrige la ruta del archivo CSV
df = pd.read_csv('Ejercicios 2/diabetes.csv')

# Selecciona solo la columna 'BMI'
X = df[['BMI']]

w = 0.09
b = -3.6

x = np.linspace(X['BMI'].min(), X['BMI'].max(), 1000)
y = 1 / (1 + np.exp(-(w * x + b)))

plt.scatter(X['BMI'], df['Outcome'])  # Usa df['Outcome'] para la variable dependiente
plt.plot(x, y)

plt.show()
