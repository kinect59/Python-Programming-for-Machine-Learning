# MNIST in Keras

# Loading MNIST dataset in Keras.
from keras.datasets import mnist
from keras.utils import to_categorical

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Checking data size.
print(train_images.shape)
print(len(train_labels))

print(test_images.shape)
print(len(test_labels))

# Preparing data to train.
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

# Preparing the labels.
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)


# Building a simple neural network.
from keras import models
from keras import layers

network = models.Sequential()
network.add(layers.Dense(512, activation = 'relu', input_shape = (28 * 28,)))
network.add(layers.Dense(10, activation = 'softmax'))

network.compile(optimizer = 'rmsprop',
                loss = 'categorical_crossentropy',
                metrics = ['accuracy'])

# Starting to train your network on the MNIST dataset.
network.fit(train_images, train_labels, epochs = 10, batch_size = 128, verbose=2)

# Evaluating on the test set.
test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test accuracy:', test_acc, '%' )
