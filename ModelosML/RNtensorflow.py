import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
import tensorflow._api.v2.compat.v1 as tf
tf.disable_v2_behavior()

# Dos anillos concéntricos de datos. 
X, Y = datasets.make_circles(n_samples=500, factor=0.5, noise=0.05)

# Resolución del mapa de predicción.
res = 100

# Coordendadas del mapa de predicción.
_x0 = np.linspace(-3, 3, res)
_x1 = np.linspace(-3, 3, res)

# Input con cada combo de coordenadas del mapa de predicción.
_pX = np.array(np.meshgrid(_x0, _x1)).T.reshape(-1, 2)


# Definimos los puntos de entrada de la red, para la matriz X e Y.
iX = tf.placeholder(dtype='float', shape=[None, X.shape[1]])
iY = tf.placeholder(dtype='float', shape=[None])

# Capas
nn = [2, 16, 8, 4, 1]

l=iX

for i in range(len(nn)-1):
  
  W = tf.Variable(tf.random_normal([nn[i], nn[i+1]]))
  b = tf.Variable(tf.random_normal([nn[i+1]]))

  prod=tf.add(tf.matmul(l, W), b)

  if i == len(nn)-2:
     # capa de salida
     l = tf.nn.sigmoid(prod)[:,0]
  else:
      # Capas ocultas
     l = tf.nn.relu(prod)

# for i in range(len(nn)-1):
    
#   l = tf.layers.dense(inputs=l, units=nn[i+1], activation=tf.nn.relu if i < len(nn)-2 else tf.nn.sigmoid)

# # Evaluación de las predicciones.
# loss = tf.losses.mean_squared_error(l[:, 0], iY)

# Evaluación de las predicciones.
loss = tf.losses.mean_squared_error(l, iY)

# Definimos al optimizador de la red, para que minimice el error.
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.05).minimize(loss)

# Número de ciclos de entrenamiento.
n_steps = 1000 

# Aquí guardaremos la evolución de las predicción, para la animación.
iPY = [] 
_pY = np.zeros((res, res))
with tf.Session() as sess:
  
  # Inicializamos todos los parámetros de la red, las matrices W y b.
  sess.run(tf.global_variables_initializer())
    
  # Iteramos n pases de entrenamiento.
  for step in range(n_steps):
  
    # Evaluamos al optimizador, a la función de coste y al tensor de salida pY. 
    # La evaluación del optimizer producirá el entrenamiento de la red.
    _, _loss, _pY = sess.run([optimizer, loss, l], feed_dict={ iX : X, iY : Y })
    
    # Cada 25 iteraciones, imprimimos métricas.
    if step % 25 == 0: 
      
      # Obtenemos predicciones para cada punto de nuestro mapa de predicción _pX.
      _pY = sess.run(l, feed_dict={ iX : _pX }).reshape((res, res))

      # Y lo guardamos para visualizar la animación.
      iPY.append(_pY)

print("--- Generando animación ---")

pY = np.array(iPY[-1])

# Visualización del mapa de predicción.
plt.figure(figsize=(10,10))

plt.pcolormesh(_x0, _x1, pY, cmap="coolwarm")

# Visualización de la nube de datos.
plt.scatter(X[:,0], X[:,1], c=Y)

plt.show()