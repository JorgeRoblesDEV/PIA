import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

# Datos de entrada
X = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

print(y)  # Muestra las etiquetas de clasificación

logistc = linear_model.LogisticRegression()  # Crear modelo de regresión logística
logistc.fit(X, y)  # Ajustar el modelo a los datos de entrada

print(logistc.intercept_)
print(logistc.coef_)

# Crear un conjunto de datos de prueba para visualizar la curva de probabilidad
X_test = np.linspace(X.min(), X.max(), 1000).reshape(-1, 1)

# Realizar predicciones de probabilidad en el conjunto de prueba
predict = logistc.predict_proba(X_test)
print(predict)
predict = logistc.predict_proba(X_test)[:,1]
print(predict)

# Graficar la curva de probabilidad
plt.plot(X_test, predict, color='green')

# Clasificar los puntos según sus etiquetas y colorearlos
plt.scatter(X[y == 0], y[y == 0], color='blue', label='No Cancerosos')  # Puntos no cancerosos en azul
plt.scatter(X[y == 1], y[y == 1], color='red', label='Cancerosos')  # Puntos cancerosos en rojo

plt.legend()  # Mostrar leyenda con los colores
plt.show()