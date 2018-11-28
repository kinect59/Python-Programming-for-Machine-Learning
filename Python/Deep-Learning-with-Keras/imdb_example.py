""" Program description: Classifying movie reviews from the IMDB dataset in Keras. """


# Load library.
import numpy as np
from keras.datasets import imdb
from keras import models
from keras import layers

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

# Word_index is a dictionary mapping words to an integer index.
word_index = imdb.get_word_index()

# We reverse it, mapping integer indices to words.
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

# We decode the review; note that our indices were offset by 3.
decoded_review = ' '.join([reverse_word_index.get(i - 3, '?') for i in train_data[0]])

def vectorize_sequences(sequences, dimension=10000):
    # Create an all-zero matrix of shape (len(sequences), dimension)
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.  # set specific indices of results[i] to 1s
    return results

# Our vectorized training data.
x_train = vectorize_sequences(train_data)
# Our vectorized test data
x_test = vectorize_sequences(test_data)

# Our vectorized labels.
y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(test_labels).astype('float32')

# Defining a DNN with three layers.

model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

x_val = x_train[:10000]
partial_x_train = x_train[10000:]

y_val = y_train[:10000]
partial_y_train = y_train[10000:]

# Training.
History = model.fit(partial_x_train,
                    partial_y_train,
                    epochs=20,
                    batch_size=512,
                    validation_data=(x_val, y_val))

# Plotting the training and validation loss/acc.

""" In Keras, model.fit() returns a History object, this object has history member that is a dictionary containing data about the training process."""

# Call history member.
history_dict = History.history


# Plotting loss.
import matplotlib.pyplot as plt

loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']
epochs = range(1, 21) # From 1 to 20 

plt.plot(epochs, loss_values, 'bo', label = 'Training loss' )
plt.plot(epochs, val_loss_values, '*', label = 'Validation loss')
plt.title("Training and Validation Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend() # A method which is used to find out the best place in the figure.
plt.show()

# Plotting accuracies.

plt.clf() # For clearing the previous figure.
acc_values = history_dict['acc']
val_acc_values = history_dict['val_acc']


plt.plot(epochs, acc_values, 'bo', label = 'Training accuracy' )
plt.plot(epochs, val_acc_values, '*', label = 'Validation accuracy')
plt.title("Training and Validation Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Acc.")
plt.legend() # A method which is used to find out the best place in the figure.
plt.show()
