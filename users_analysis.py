import json
import matplotlib.pyplot as plt
import numpy as np
from tkinter import Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

with open('customers_data.json', 'r', encoding='utf-8') as json_file:
    users_data = json.load(json_file)

print(type(users_data))

# Розділіть дані на роки та кількість користувачів
str_years = list(users_data.keys())
users_count = list(users_data.values())
years = [int(i) for i in str_years]
years, users_count = zip(*sorted(zip(years, users_count)))
print(f'{years}\n{users_count} \n')

# Пункт 1: Візуалізація даних
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(years, users_count, marker='o', linestyle='-', color='b', label='Реальні дані')  # Додайте легенду для реальних даних
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

# Додаємо графік до Tkinter вікна
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill='both', expand=True)

root.mainloop()
