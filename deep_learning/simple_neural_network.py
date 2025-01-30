import tensorflow as tf
from tensorflow import keras

# Define the model
model = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(784,)),  # Hidden layer
    keras.layers.Dense(10, activation='softmax')  # Output layer (10 classes)
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model (Example with dummy data)
import numpy as np
x_train = np.random.rand(60000, 784)
y_train = np.random.randint(0, 10, 60000)
model.fit(x_train, y_train, epochs=5)
