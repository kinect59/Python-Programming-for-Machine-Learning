
"""
Program description: K-fold validation and training the final DL model in Python/Keras.
"""

# Load library and packages.
from keras.datasets import boston_housing
(train_data, train_labels), (test_data, test_labels) = boston_housing.load_data()

print(train_data.shape)
print(test_data.shape)

# Normalizing data.
mean = train_data.mean(axis=0) # Using numpy array.
train_data -= mean # Subtract mean.
std = train_data.std(axis=0)
train_data /= std # Divide standard deviation

test_data -= mean # Using mean and std from training set.
test_data /= std


# Building deep learning model.
from keras import models
from keras import layers
from keras.models import load_model

def build_model(): # Using the same model multipe times.
    model = models.Sequential()
    model.add(layers.Dense(64, activation = 'relu', input_shape = (train_data.shape[1],)))
    model.add(layers.Dense(64, activation = 'relu'))
    model.add(layers.Dense(1)) # No activation function, learn to predict values in nay ranges.
    model.compile(optimizer='rmsprop', loss = 'mse', metrics = ['mae'])
    return model

'''
Mean Squared Error (MSE) is a widely used loss function for regression problem.
Mean Absolute Error (MAE) is used for monotoring the model performance.
'''

# Training on K-fold
import numpy as np

k = 4
num_val_samples = len(train_data) // k
num_epochs = 100
all_score = []

for i in range(k):
    print('Processing fold #', i)
    val_data = train_data[i * num_val_samples: (i+1) * num_val_samples]
    val_labels = train_labels[i * num_val_samples: (i+1) * num_val_samples]

    partial_train_data = np.concatenate(
        [train_data[: i * num_val_samples],
        train_data[(i + 1) * num_val_samples:]], axis = 0)

    partical_train_labels = np.concatenate(
        [train_labels[: i * num_val_samples],
        train_labels[(i + 1) * num_val_samples:]], axis = 0)

    regression_model = build_model()

    regression_model.fit(partial_train_data, partical_train_labels, epochs = num_epochs, batch_size = 1, verbose = 2)


    # Saving model.
    """
    Saving whole keras model (architecture + weights + optimizer state)
    It is not recommended to use picke to sava Keras model.
    The model of Keras has a save method, which is used to save all the details necessary to reconstitute the model. 
    """

    regression_model.save("model_fold_k_{0}.h5".format(i))
    val_mse, val_mae = regression_model.evaluate(val_data, val_labels, verbose = 0)
    all_score.append(val_mae)
    del regression_model
    
# Compute the average of the scores for k-fold. 

print(np.mean(all_score))


# Training the final model. All trained models with K-fold have been discarded. They are no longer needed. 
# They have served their purpose to help you choose a best learning model with its hyperparameters. 
# Now, you need to train your choose model on the full training dataset.
model = build_model()

model.fit(train_data, train_labels, epochs = 100, batch_size = 16, verbose = 2)

test_mse_score, test_mae_score = model.evaluate(test_data, test_labels)

print(test_mae_score)







