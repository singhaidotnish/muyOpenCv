"""
#Building a neural network from scratch involves implementing the forward and backward propagation steps,
along with weight updates using an optimization algorithm. Below is a simple implementation using Python and NumPy.

Steps to Build a Neural Network
    +----------------------------------+----------------------------------------------------------------------------------+
    |   Parameter                      |    Description                                                                   |
    +==================================+==================================================================================+
    |   Initialize Parameters          |    Randomly initialize weights and biases.                                       |
    +----------------------------------+----------------------------------------------------------------------------------+
    |   Forward Propagation            |    Compute activations through the layers.                                       |
    +----------------------------------+----------------------------------------------------------------------------------+
    |   Loss Calculation               |    Measure error using a loss function.                                          |
    +----------------------------------+----------------------------------------------------------------------------------+
    |   Backward Propagation           |    Compute gradients and update weights.                                         |
    +----------------------------------+----------------------------------------------------------------------------------+
    |   Train the Network              |    Iterate through multiple epochs.                                              |
    +----------------------------------+----------------------------------------------------------------------------------+
"""

# Implementation
# Let's build a basic feedforward neural network with one hidden layer.

# Step 1: Import Dependencies

import numpy as np

# Step 2: Initialize Parameters

def initialize_parameters(input_size, hidden_size, output_size):
    '''
    Randomly initialize weights and biases.
    :param input_size:
    :param hidden_size:
    :param output_size:
    :return:
    '''
    np.random.seed(42)  # Ensures reproducibility
    W1 = np.random.randn(hidden_size, input_size) * 0.01
    b1 = np.zeros((hidden_size, 1))
    W2 = np.random.randn(output_size, hidden_size) * 0.01
    b2 = np.zeros((output_size, 1))

    return {"W1": W1, "b1": b1, "W2": W2, "b2": b2}

# Step 3: Activation Functions

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def relu(z):
    return np.maximum(0, z)

def relu_derivative(z):
    return z > 0

# Step 4: Forward Propagation

def forward_propagation(X, parameters):
    '''
    Compute activations through the layers.
    :param X:
    :param parameters:
    :return:
    '''
    W1, b1, W2, b2 = parameters["W1"], parameters["b1"], parameters["W2"], parameters["b2"]
    
    Z1 = np.dot(W1, X) + b1
    A1 = relu(Z1)
    Z2 = np.dot(W2, A1) + b2
    A2 = sigmoid(Z2)
    
    cache = {"Z1": Z1, "A1": A1, "Z2": Z2, "A2": A2}
    return A2, cache

# Step 5: Compute Loss

def compute_loss(Y, A2):
    '''
    Measure error using a loss function.
    :param Y:
    :param A2:
    :return:
    '''
    m = Y.shape[1]  # Number of examples
    loss = -np.mean(Y * np.log(A2) + (1 - Y) * np.log(1 - A2))
    return loss

# Step 6: Backward Propagation

def backward_propagation(X, Y, parameters, cache):
    '''
    Compute gradients and update weights.
    :param X:
    :param Y:
    :param parameters:
    :param cache:
    :return:
    '''
    m = X.shape[1]
    W2 = parameters["W2"]

    A1, A2 = cache["A1"], cache["A2"]
    Z1 = cache["Z1"]

    dZ2 = A2 - Y
    dW2 = np.dot(dZ2, A1.T) / m
    db2 = np.sum(dZ2, axis=1, keepdims=True) / m

    dA1 = np.dot(W2.T, dZ2)
    dZ1 = dA1 * relu_derivative(Z1)
    dW1 = np.dot(dZ1, X.T) / m
    db1 = np.sum(dZ1, axis=1, keepdims=True) / m

    gradients = {"dW1": dW1, "db1": db1, "dW2": dW2, "db2": db2}
    return gradients

# Step 7: Update Parameters

def update_parameters(parameters, gradients, learning_rate=0.01):
    '''

    :param parameters:
    :param gradients:
    :param learning_rate:
    :return:
    '''
    parameters["W1"] -= learning_rate * gradients["dW1"]
    parameters["b1"] -= learning_rate * gradients["db1"]
    parameters["W2"] -= learning_rate * gradients["dW2"]
    parameters["b2"] -= learning_rate * gradients["db2"]
    
    return parameters

# Step 8: Training Loop

def train(X, Y, input_size, hidden_size, output_size, epochs=1000, learning_rate=0.01):
    '''
    Iterate through multiple epochs.
    :param X:
    :param Y:
    :param input_size:
    :param hidden_size:
    :param output_size:
    :param epochs:
    :param learning_rate:
    :return:
    '''
    parameters = initialize_parameters(input_size, hidden_size, output_size)

    for i in range(epochs):
        A2, cache = forward_propagation(X, parameters)
        loss = compute_loss(Y, A2)
        gradients = backward_propagation(X, Y, parameters, cache)
        parameters = update_parameters(parameters, gradients, learning_rate)

        if i % 100 == 0:
            print(f"Epoch {i}, Loss: {loss:.4f}")
    
    return parameters



# Testing the Neural Network

# Generate some dummy data (X: 2 input features, Y: binary labels)
np.random.seed(42)
X = np.random.randn(2, 1000)
Y = (np.sum(X, axis=0) > 0).reshape(1, 1000)  # Simple classification rule

# Train the model
parameters = train(X, Y, input_size=2, hidden_size=4, output_size=1, epochs=1000, learning_rate=0.1)

# This simple neural network learns a decision boundary between two classes.
# You can extend it by adding more layers, using better activation functions,
# or implementing optimizers like Adam.
