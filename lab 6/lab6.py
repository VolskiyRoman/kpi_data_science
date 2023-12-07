import numpy as np
import matplotlib.pyplot as plt

# Вхідні дані
inputs = np.array([[0, 1, 1],
                   [0, 0, 0],
                   [1, 0, 0],
                   [1, 0, 1],
                   [0, 0, 1]])

# Вихідні дані
outputs = np.array([[0], [0], [0], [1], [1]])

# Клас NeuralNetwork, який використовує матричні операції
class NeuralNetwork:
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs
        self.weights = np.random.rand(inputs.shape[1], 1)  # Ініціалізуємо ваги випадковими значеннями
        self.bias = np.zeros((1, 1))  # Зсув
        self.learning_rate = 0.1
        self.error_history = []

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def feed_forward(self):
        self.hidden = self.sigmoid(np.dot(self.inputs, self.weights) + self.bias)

    def backpropagation(self):
        error = self.outputs - self.hidden
        d_weights = np.dot(self.inputs.T, error * self.sigmoid_derivative(self.hidden))
        d_bias = np.sum(error * self.sigmoid_derivative(self.hidden), keepdims=True)
        self.weights += self.learning_rate * d_weights
        self.bias += self.learning_rate * d_bias

    def train(self, epochs=10000):
        for epoch in range(epochs):
            self.feed_forward()
            self.backpropagation()
            self.error_history.append(np.mean(np.abs(self.outputs - self.hidden)))

    def predict(self, new_input):
        return self.sigmoid(np.dot(new_input, self.weights) + self.bias)

# Ініціалізація та тренування мережі
nn = NeuralNetwork(inputs, outputs)
nn.train()

# Перевірка результатів
test_inputs = np.array([[0, 1, 1], [1, 1, 0]])
for test_input in test_inputs:
    prediction = nn.predict(test_input)
    print(f'Input: {test_input}, Predicted Output: {prediction}')

# Динаміка зміни помилки з часом тренування
plt.figure(figsize=(8, 4))
plt.plot(nn.error_history)
plt.xlabel('Epoch')
plt.ylabel('Error')
plt.title('Training Error Over Time')
plt.show()


