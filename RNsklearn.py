import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.neural_network import MLPClassifier

# Creamos nuestros datos artificiales, donde buscaremos clasificar 
# dos anillos concéntricos de datos. 
X, Y = make_circles(n_samples=500, factor=0.5, noise=0.05)

# Resolución del mapa de predicción.
res = 100 

# Coordendadas del mapa de predicción.
_x0 = np.linspace(-1.5, 1.5, res)
_x1 = np.linspace(-1.5, 1.5, res)

# Input con cada combo de coordenadas del mapa de predicción.
_pX = np.array(np.meshgrid(_x0, _x1)).T.reshape(-1, 2)

lr = 0.01           # learning rate
nn = [2, 16, 8, 1]  # número de neuronas por capa.

# Creamos el objeto del modelo de red neuronal multicapa.
clf = MLPClassifier(solver='sgd', 
                    learning_rate_init=lr, 
                    hidden_layer_sizes=tuple(nn[1:]),
                    n_iter_no_change=1000,
                    batch_size = 64)

# Y lo entrenamos con nuestros datos.
clf.fit(X, Y)

# Obtener predicciones para el mapa de predicción.
_pY = clf.predict_proba(_pX)[:, 1].reshape(res, res)

# Visualización del mapa de predicción.
plt.figure(figsize=(8, 8))
plt.pcolormesh(_x0, _x1, _pY, cmap="coolwarm", vmin=0, vmax=1)
plt.scatter(X[:,0], X[:,1], c=Y)
plt.show()
