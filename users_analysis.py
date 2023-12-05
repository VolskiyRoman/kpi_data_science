import json
from datetime import timedelta

import matplotlib.pyplot as plt
import numpy as np
from tkinter import Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def generate_and_analyze_synthetic_data(dates, real_inflation_values, is_printed, predict,
                                        degree=15):
    noise_std = 0.3

    np.random.seed(0)
    coefficients = np.polyfit(np.arange(len(dates)), real_inflation_values, degree)
    if predict:
        last_date = max(dates)
        additional_dates = [last_date + timedelta(days=365 * i) for i in range(1, 6)]
        dates += additional_dates
        synthetic_trend_values = np.polyval(coefficients, np.arange(len(dates)))
    else:
        synthetic_trend_values = np.polyval(coefficients, np.arange(len(dates)))
    print("\nМодель:")
    print(np.poly1d(coefficients))
    synthetic_inflation_values = synthetic_trend_values + np.random.normal(0, noise_std, len(dates))

    if is_printed:
        synthetic_mean_inflation = np.mean(synthetic_inflation_values)
        synthetic_std_deviation_inflation = np.std(synthetic_inflation_values)
        synthetic_median_inflation = np.median(synthetic_inflation_values)
        synthetic_min_inflation = np.min(synthetic_inflation_values)
        synthetic_max_inflation = np.max(synthetic_inflation_values)
        synthetic_variance_inflation = np.var(synthetic_inflation_values)

        print("\nSynthetic Data Statistics:")
        print("Mean inflation value:", synthetic_mean_inflation)
        print("Standard deviation of inflation:", synthetic_std_deviation_inflation)
        print("Median inflation:", synthetic_median_inflation)
        print("Minimum inflation value:", synthetic_min_inflation)
        print("Maximum inflation value:", synthetic_max_inflation)
        print("Inflation variance:", synthetic_variance_inflation)

    return synthetic_trend_values, synthetic_inflation_values


if __name__ == '__main__':
    with open('customers_data.json', 'r', encoding='utf-8') as json_file:
        users_data = json.load(json_file)

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

    predicted_users_count = [p(i) for i in range(2010, 2023)]

    ax.plot(range(2010, 2023), predicted_users_count, marker='o', linestyle='--', color='r', label='Лінія тренду')

    ax.legend()

    root = Tk()
    root.title('Графік активних користувачів YouTube')
    root.geometry('800x600')

    # Додаємо графік до Tkinter вікна
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill='both', expand=True)

    root.mainloop()
