import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
import numpy as np

df = pd.read_csv("data.csv")

X = df[['Weight','Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

warr = np.linspace(X.Weight.min(), X.Weight.max(), 100)
varr = np.linspace(X.Volume.min(), X.Volume.max(), 100)

cwarr = warr.reshape(-1, 1)
cvarr = varr.reshape(-1, 1)

arr = np.concatenate((cwarr,cvarr), axis=1)

print(arr)
pred = regr.predict(arr)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(X.Weight, X.Volume, y)
ax.set_xlabel('Weight (kg)')
ax.set_ylabel('Volume (cm3)')
ax.set_zlabel('CO2')

# Saca el plano del gráfico 3D
pred = regr.predict(arr)
ax.plot(warr, varr, pred, alpha=0.5, color='red')

plt.show()

