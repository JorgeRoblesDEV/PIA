import numpy as np
import matplotlib.pyplot as plt
import tensorflow._api.v2.compat.v1 as tf
import NeuralNet as nt
from matplotlib import animation

# IMPORTAR LIBRERÍAS NECESARIAS AQUÍ ######################
from sklearn.datasets import make_circles
# INSERTAR CÓDIGO AQUÍ PRIMERA TAREA#######################
X,trainY = make_circles(n_samples=500, factor=0.5, noise=0.05)

res = 100
min_coord = np.min(X)
max_coord = np.max(X)

print(min_coord)
print(max_coord)
###########################################################
_x0 = np.linspace(min_coord, max_coord, res)
_x1 = np.linspace(max_coord, min_coord, res)
pX = np.array(np.meshgrid(_x0, _x1)).T.reshape(-1, 2)

tf.disable_v2_behavior()

# INSERTAR CÓDIGO TERCERA TAREA AQUÍ ######################
trainX, Y = make_circles(n_samples=500, factor=0.5, noise=0.05)

res = 100

iX = tf.placeholder('float', shape=[None, X.shape[1]])
iY = tf.placeholder('float', shape=[None])

testX = np.array(np.meshgrid(_x0, _x1)).T.reshape(-1, 2)

topology_vector = [2, 4, 4, 1]



_pX = np.array(np.meshgrid(_x0, _x1)).T.reshape(-1, 2)

_pY = np.zeros((res, res))

current_layer = iX


pY = current_layer[:, 0]

loss = tf.losses.mean_squared_error(pY, iY)

lr = 0.01
optimizer = tf.train.GradientDescentOptimizer(lr).minimize(loss)

n_steps = 10000
###########################################################

nn = nt.NeuralNet()
nn.create_nn(topology_v=topology_vector, lr=lr)

iPY = []

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(n_steps):
        _, _loss, _pY = sess.run([nn.optimizer, nn.loss, nn.pY], feed_dict={nn.iX: trainX, nn.iY: trainY})
        if step % 25 == 0:
            acc = np.mean(np.round(_pY) == trainY)
            print('Step', step, '/', n_steps, '- Loss = ', _loss, '- Acc =', acc)
            _pY = sess.run(nn.pY, feed_dict={nn.iX: testX}).reshape((res, res))
            iPY.append(_pY.T)

print("--- Generando animación ---")

ims = []
fig = plt.figure(figsize=(10, 10))
for fr in range(len(iPY)):
    im = plt.pcolormesh(_x0, _x1, iPY[fr], cmap="coolwarm", animated=True)
    plt.scatter(X[Y == 0, 0], X[Y == 0, 1], c="skyblue")
    plt.scatter(X[Y == 1, 0], X[Y == 1, 1], c="salmon")
    plt.tick_params(labelbottom=False, labelleft=False)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)

ani.save('animation.gif', writer=animation.PillowWriter())
