import json
import matplotlib.pyplot as plt
import numpy as np
from tkinter import Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

with open('customers_data.json', 'r', encoding='utf-8') as json_file:
    users_data = json.load(json_file)

print(type(users_data))

str_years = list(users_data.keys())
users_count = list(users_data.values())
years = [int(i) for i in str_years]
years, users_count = zip(*sorted(zip(years, users_count)))
print(f'{years}\n{users_count} \n')

# Пункт 1: Візуалізація даних
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(years, users_count, marker='o', linestyle='-', color='b', label='Реальні дані')
ax.set_title('Динаміка активних користувачів YouTube (в мільярдах)')
ax.set_xlabel('Рік')
ax.set_ylabel('Кількість користувачів (мільярди)')
ax.grid(True)

# Додаємо прогнозований графік
z = np.polyfit(years, users_count, 1)
p = np.poly1d(z)  # Створюємо лінійну функцію
print(p)

predicted_users_count = []
future_years = range(2010, 2023)

for i in future_years:
    predicted_users = p(i)
    predicted_users_count.append(predicted_users)

ax.plot(future_years, predicted_users_count, marker='o', linestyle='--', color='r', label='Лінія тренду')

ax.legend()

root = Tk()
root.title('Графік активних користувачів YouTube')
root.geometry('800x600')


def generate_and_analyze_synthetic_data(years, users):
    degree = 7
    noise_std = 0.5

    np.random.seed(0)
    coefficients = np.polyfit(np.arange(len(years)), users, degree)
    synthetic_trend_values = np.polyval(coefficients, np.arange(len(years)))
    print("\nModel:")
    print(np.poly1d(coefficients))
    synthetic_inflation_values = synthetic_trend_values + np.random.normal(0, noise_std, len(years))

    # Use this if you want to create anomaly
    # anomaly_index = 20
    # anomaly_value = 10.0
    # synthetic_inflation_values[anomaly_index] = anomaly_value

    synthetic_mean_inflation = np.mean(synthetic_inflation_values)
    synthetic_std_deviation_inflation = np.std(synthetic_inflation_values)
    synthetic_median_inflation = np.median(synthetic_inflation_values)
    synthetic_min_inflation = np.min(synthetic_inflation_values)
    synthetic_max_inflation = np.max(synthetic_inflation_values)
    synthetic_variance_inflation = np.var(synthetic_inflation_values)

    print("\nСтатистика синтетичних даних:")
    print("Середнє значення:", synthetic_mean_inflation)
    print("Стандартне відхилення:", synthetic_std_deviation_inflation)
    print("Медіана:", synthetic_median_inflation)
    print("Мінімальне значення:", synthetic_min_inflation)
    print("Максимальне значення:", synthetic_max_inflation)
    print("Дисперсія:", synthetic_variance_inflation)

    return synthetic_trend_values, synthetic_inflation_values

generate_and_analyze_synthetic_data(
        years=years,
        users=users_count)


# Додаємо графік до Tkinter вікна
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill='both', expand=True)

root.mainloop()
