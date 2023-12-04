import numpy as np

# Припустимо, що у нас є дані (роки та кількість користувачів)
years = [2010, 2011, 2012, 2013, 2014]
users_count = [0.2, 0.5, 0.7, 1.0, 1.1]

# Використовуємо метод найменших квадратів для побудови лінійного тренду
z = np.polyfit(years, users_count, 1)  # Параметр 1 вказує на лінійну функцію
p = np.poly1d(z)  # Створюємо лінійну функцію

# Прогноз значення користувачів у 2016 році
year_to_predict = 2020
predicted_users_count = p(year_to_predict)
print(f"Прогноз користувачів у {year_to_predict} році: {predicted_users_count}")
