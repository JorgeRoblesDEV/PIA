import numpy as np
import matplotlib.pyplot as plt

# IMPORTAR LIBRERÍAS NECESARIAS AQUÍ ######################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import r2_score
###########################################################

X = np.arange(0, 20, 0.2)
y = np.cos(X)

# INSERTAR CÓDIGO AQUÍ ####################################
def calc_r_model(grado):
    model = np.poly1d(np.polyfit(X, y, grado))
    return r2_score(y, model(X)), model

grado = 0
porcentaje = 90
coef_deter = porcentaje / 100

r, model = calc_r_model(grado)
while r < coef_deter:
    grado = grado + 1
    r, model = calc_r_model(grado)

print("R² de grado " + str(grado) + ": ", r2_score(y, model(X)))

line = np.linspace(X.min(), X.max(), num=1000)

plt.scatter(X, y)
plt.plot(line, model(line), label="Regresion")
plt.title("Regresion Polinomial de grado " + str(grado))
plt.xlabel("X tiempo")
plt.ylabel("Y Amplitud")

plt.legend(loc="upper right")
###########################################################

plt.show()
