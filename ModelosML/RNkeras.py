import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles

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

# Objeto vacío a 0.5 del mapa de predicción.
_pY = np.random.rand(res, res)

# Learning rate y número de neuronas por capa.
nn = [2, 32, 16, 1] 

# Creamos el objeto que contendrá a nuestra red neuronal.
model = tf.keras.Sequential()

# Añadir la capa de entrada
model.add(tf.keras.layers.InputLayer(input_shape=(2,)))

# Añadir la capa 1
model.add(tf.keras.layers.Dense(nn[1], activation='relu'))

# Añadir la capa 2
model.add(tf.keras.layers.Dense(nn[2], activation='relu'))

# Añadir la capa 3
model.add(tf.keras.layers.Dense(nn[3], activation='sigmoid'))

# Compilamos el modelo, definiendo la función de pérdida y el optimizador.
model.compile(loss='binary_crossentropy', optimizer=tf.keras.optimizers.SGD(lr=0.05), metrics=['acc'])

# Número de épocas
model.fit(X, Y, epochs=1000)

# Obtener predicciones para el mapa de predicción
predictions = model.predict(_pX)
    
# Actualizar el mapa de predicción con las nuevas predicciones
_pY = predictions.reshape(res, res)

# Visualización del mapa de predicción después del entrenamiento.
plt.figure(figsize=(8, 8))
plt.pcolormesh(_x0, _x1, _pY, cmap="coolwarm")
plt.scatter(X[:,0], X[:,1], c=Y)
plt.show()
