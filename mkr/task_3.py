import numpy as np
import matplotlib.pyplot as plt

# Задаємо параметри моделі
amplitude = 10  # Амплітуда періодичного сигналу
frequency = 0.1  # Частота періодичного сигналу
mean = 0  # Середнє значення нормального розподілу похибок
std_dev = 2  # Стандартне відхилення нормального розподілу похибок
num_points = 100  # Кількість точок в датасеті

# Генеруємо періодичний сигнал
time = np.linspace(0, 10, num_points)  # Від 0 до 10 з 100 рівномірно розподіленими точками
periodic_signal = amplitude * np.sin(2 * np.pi * frequency * time)

# Генеруємо нормально розподілені похибки
errors = np.random.normal(mean, std_dev, num_points)

# Сумуємо сигнал та похибки, щоб отримати модель виміру
measurement_model = periodic_signal + errors

# Побудова графіків
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(time, periodic_signal, label='Періодичний сигнал')
plt.title('Періодичний сигнал')

plt.subplot(3, 1, 2)
plt.plot(time, errors, label='Похибки')
plt.title('Нормально розподілені похибки')

plt.subplot(3, 1, 3)
plt.plot(time, measurement_model, label='Модель виміру')
plt.title('Модель виміру з періодичним сигналом та похибками')

plt.tight_layout()
plt.show()
