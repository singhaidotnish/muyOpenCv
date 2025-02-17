### To train models using TensorFlow/Keras or PyTorch, follow these general steps:

**1️⃣ Using TensorFlow/Keras
Keras (part of TensorFlow) provides a high-level API for deep learning.**

**Step 1: Install TensorFlow**

pip install tensorflow

**Step 2: Import Libraries**

import tensorflow as tf 
from tensorflow import keras
from tensorflow.keras import layers

**Step 3: Load & Prepare Data (e.g., MNIST)**

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0  # Normalize


**Step 4: Define Model**

model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Input layer
    layers.Dense(128, activation='relu'),  # Hidden layer
    layers.Dropout(0.2),  # Prevent overfitting
    layers.Dense(10, activation='softmax')  # Output layer
])

**Step 5: Compile Model**

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

**Step 6: Train Model**

model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

**Step 7: Evaluate & Save Model**

test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc}")

model.save("mnist_model.h5")  # Save model


**2️⃣ Using PyTorch
PyTorch provides more flexibility, useful for research and advanced use cases.**


**Step 1: Install PyTorch**

pip install torch torchvision

**Step 2: Import Libraries**

import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

**Step 3: Load & Prepare Data**

transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

trainset = torchvision.datasets.MNIST(root='./data', train=True, transform=transform, download=True)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

testset = torchvision.datasets.MNIST(root='./data', train=False, transform=transform, download=True)
testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=False)

**Step 4: Define Model**

class NeuralNet(nn.Module):
    def __init__(self):
        super(NeuralNet, self).__init__()
        self.fc1 = nn.Linear(28*28, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = x.view(-1, 28*28)  # Flatten input
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

model = NeuralNet()

**Step 5: Define Loss & Optimizer**

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

**Step 6: Train Model**

for epoch in range(5):  # Train for 5 epochs
    for images, labels in trainloader:
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item()}")

**Step 7: Evaluate Model**

correct = 0
total = 0
with torch.no_grad():
    for images, labels in testloader:
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f"Test Accuracy: {100 * correct / total}%")

Which One Should You Use?


| Feature              | TensorFlow/Keras              | PyTorch                       |
| -------------------- | ------------------------------ |------------------------------|
| Ease of Use          | ✅ High (Beginner-Friendly)    | ❌ Medium (More Code)          |
| Flexibility          | ❌ Medium (High-Level API)     | ✅ High (More Customization)   |
| Performance          | ✅ Optimized                   | ✅ Optimized                   |
| Research & Debugging | ❌ Harder	                   | ✅ Easier                      |



Use TensorFlow/Keras if you want a high-level API that’s easy to use.
Use PyTorch if you need more control and flexibility.