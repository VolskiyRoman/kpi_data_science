import numpy as np
import json

# Завантаження уявних даних із файлу у форматі JSON
with open('housing_data.json', 'r', encoding='utf-8') as file:
    housing_data = json.load(file)

# Кількість аналогічних товарів
num_of_products = len(housing_data)

# Визначення критеріїв та їх значень
maximized_criteria = ['площа', 'локація', 'зручність транспортного сполучення', 'інфраструктура']
minimized_criteria = ['вартість', 'вартість утримання', 'екологічність', 'рівень кримінальності',
                       'сервісні послуги', 'доступність закладів освіти', 'безпека району', 'екологічна зона']

# Створення матриці, де рядки представляють аналогічні товари, а стовпці - критерії
matrix = np.random.rand(num_of_products, len(maximized_criteria) + len(minimized_criteria))

# Розділення матриці на максимізовані та мінімізовані критерії
maximized_matrix = matrix[:, :len(maximized_criteria)]
minimized_matrix = matrix[:, len(maximized_criteria):]

# Збільшення ваги останнього критерію максимізації
maximized_matrix[:, -1] *= 100

# Розрахунок сумарних балів для кожного товару на основі ваг критеріїв
weighted_sum = np.sum(maximized_matrix, axis=1) - np.sum(minimized_matrix, axis=1)

# Вивід результатів
for i, score in enumerate(weighted_sum):
    product_name = f"Товар {i + 1}"
    print(f"{product_name}: Загальний бал - {score}")
