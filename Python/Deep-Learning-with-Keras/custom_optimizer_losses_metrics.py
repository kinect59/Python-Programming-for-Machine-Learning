
""" Program description: Create three-layer neural network in Keras """

from keras import models
from keras import layers


model = models.Sequential()
model.add(layers.Dense(16, activation = 'relu', input_shape = (1000,)))
model.add(layers.Dense(16, activation = 'relu')
model.add(layers.Dense(1, activation = 'sigmoid')


# Compile the model.
model.compile(optimizer = 'rmsprop',
              loss = 'binary_crossentropy',  # The term of 'entropy' is come from the field of Information Theory, which is used to mesure the distance between two probability distributios.
              metrics = 'accuracy')


# How to use your custom optimizers and losses and metrics.
from keras import optimizers
from keras import losses
from keras import metrics

model.compile(optimizer = optimizers.RMSprop(lr = 0.001),
			  loss = losses.binary_crossentropy,
			  metrics = metrics.binary_accuracy)

