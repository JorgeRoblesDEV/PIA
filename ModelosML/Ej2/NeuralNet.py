import tensorflow._api.v2.compat.v1 as tf

class NeuralNet:
# INSERTAR CÓDIGO AQUÍ SEGUNDA TAREA#######################
    pass

    def __init__(self):
        self.iX = 0
        self.iY = 0
        self.pY = 0
        self.loss = 0
        self.optimizer = 0

    def create_nn(self, topology_vector, lr):
        activations = [tf.nn.relu, tf.nn.relu, tf.nn.sigmoid]
        for i in range(len(topology_vector) - 1):
            current_layer = self.create_layer(current_layer, topology_vector[i], topology_vector[i + 1], activations[i])
    def create_layer(input_layer, input_size, output_size, activation):
        W = tf.Variable(tf.random_normal([input_size, output_size]))
        b = tf.Variable(tf.random_normal([output_size]))
        layer = activation(tf.add(tf.matmul(input_layer, W), b))
        return layer

###########################################################
