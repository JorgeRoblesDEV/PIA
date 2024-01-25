import numpy as np
import tensorflow._api.v2.compat.v1 as tf
tf.disable_v2_behavior()
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
_pY = np.zeros((res, res))

# Definimos los puntos de entrada de la red, para la matriz X e Y.
iX = tf.placeholder('float', shape=[None, X.shape[1]])
iY = tf.placeholder('float', shape=[None])

nn = [2, 15, 10, 6, 5, 4, 4, 1]  # número de neuronas por capa.
activations = [tf.nn.relu] * (len(nn) - 2) + [tf.nn.sigmoid]  # Funciones de activación por capa.
# activations = [tf.nn.relu, tf.nn.relu, tf.nn.relu, tf.nn.relu, tf.nn.sigmoid]  # Funciones de activación por capa.

# Crear dinámicamente las capas de la red
def create_layer(input_layer, input_size, output_size, activation):
    W = tf.Variable(tf.random_normal([input_size, output_size]))
    b = tf.Variable(tf.random_normal([output_size]))
    layer = activation(tf.add(tf.matmul(input_layer, W), b))
    return layer

# Construir la red
current_layer = iX

for i in range(len(nn)-1):
    current_layer = create_layer(current_layer, nn[i], nn[i+1], activations[i])


pY = current_layer[:, 0]
 
# Evaluación de las predicciones.
loss = tf.losses.mean_squared_error(pY, iY)

# Definimos al optimizador de la red, para que minimice el error.
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(loss)

n_steps = 5500  # Número de ciclos de entrenamiento.

iPY = []  # Aquí guardaremos la evolución de las predicciones para la animación.

with tf.Session() as sess:

    # Inicializamos todos los parámetros de la red, las matrices W y b.
    sess.run(tf.global_variables_initializer())

    # Iteramos n pases de entrenamiento.
    for step in range(n_steps):

        # Evaluamos al optimizador, a la función de coste y al tensor de salida pY.
        # La evaluación del optimizer producirá el entrenamiento de la red.
        _, _loss, _pY = sess.run([optimizer, loss, pY], feed_dict={iX: X, iY: Y})

        # Cada 25 iteraciones, imprimimos métricas.
        if step % 25 == 0:

            # Cálculo del accuracy.
            acc = np.mean(np.round(_pY) == Y)

            # Impresión de métricas.
            print('Step', step, '/', n_steps, '- Loss = ', _loss, '- Acc =', acc)

            # Obtenemos predicciones para cada punto de nuestro mapa de predicción _pX.
            _pY = sess.run(pY, feed_dict={iX: _pX}).reshape((res, res))

            # Y lo guardamos para visualizar la animación.
            iPY.append(_pY)

# ----- CÓDIGO ANIMACIÓN ----- #

print("--- Generando animación ---")

pY = np.array(iPY[-1])

# Visualización del mapa de predicción.
plt.figure(figsize=(10,10))
plt.pcolormesh(_x0, _x1, pY, cmap="coolwarm")
plt.scatter(X[:,0], X[:,1], c=Y)
plt.show()