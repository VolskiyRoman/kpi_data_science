import json
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from datetime import datetime
import tkinter as tk
from sklearn.ensemble import IsolationForest
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV

from users_analysis import generate_and_analyze_synthetic_data


def evaluate_anomaly_detection_performance(parsed_inflation_values, cleaned_inflation_values):
    mse = mean_squared_error(parsed_inflation_values[:len(cleaned_inflation_values)], cleaned_inflation_values)
    rmse = np.sqrt(mse)
    return mse, rmse


if __name__ == '__main__':
    with open('customers_data.json', 'r') as file:
        customers_data = json.load(file)

    parsed_dates = [datetime.strptime(year, '%Y').date() for year in customers_data.keys()]
    parsed_values = list(customers_data.values())

    dates = parsed_dates[::-1]
    values = parsed_values[::-1]
    values[5] = 0.1

    root = tk.Tk()
    root.title("YouTube Users")

    # ______________________________________Дані______________________________________
    frame1 = tk.Frame(root)
    frame1.grid(row=0, column=0)

    fig1, ax1 = plt.subplots(figsize=(8, 4))
    ax1.plot(dates, values, marker='o', linestyle='-', color='black', markersize=4,
             label='Дані')
    ax1.set_xlabel("Дата")
    ax1.set_ylabel("Користувачі")
    plt.xticks(rotation=45)
    ax1.grid(True)
    plt.legend()
    plt.title("Графік користувачів")

    canvas1 = FigureCanvasTkAgg(fig1, master=frame1)
    canvas_widget1 = canvas1.get_tk_widget()
    canvas_widget1.pack()

    frame2 = tk.Frame(root)
    frame2.grid(row=0, column=1)

    # ______________________________________Очищені дані______________________________________
    X = np.array(values).reshape(-1, 1)
    Y = np.arange(len(dates))

    clf = IsolationForest()
    contamination_values = np.arange(0.05, 0.3, 0.05)
    param_grid = {'contamination': contamination_values}

    grid_search = GridSearchCV(clf, param_grid, cv=5, scoring='neg_mean_squared_error')

    grid_search.fit(X, Y)

    best_params = grid_search.best_params_
    print("Кращі параметри для очистки функції:", best_params)

    best_contamination = best_params['contamination']
    clf = IsolationForest(contamination=0.5)
    outliers = clf.fit_predict(X)

    cleaned_dates = [dates[i] for i in range(len(dates)) if outliers[i] == 1]
    cleaned_values = [values[i] for i in range(len(values)) if
                                outliers[i] == 1]

    fig2, ax2 = plt.subplots(figsize=(8, 4))
    ax2.plot(cleaned_dates, cleaned_values, marker='o', linestyle='-', color='blue', markersize=4,
             label='Очищені дані')
    ax2.set_xlabel("Дата")
    ax2.set_ylabel("Користувачі")
    plt.xticks(rotation=45)
    ax2.set_ylim(-2, 8)
    ax2.grid(True)
    plt.legend()
    plt.title("Графік користувачів (Очищений)")

    canvas2 = FigureCanvasTkAgg(fig2, master=frame2)
    canvas_widget2 = canvas2.get_tk_widget()
    canvas_widget2.pack()

    # ______________________________________Синтетичні дані______________________________________
    frame3 = tk.Frame(root)
    frame3.grid(row=1, column=0, columnspan=2)

    synthetic_trend_values, synthetic_inflation_values = generate_and_analyze_synthetic_data(
        dates=cleaned_dates,
        real_inflation_values=cleaned_values,
        is_printed=False,
        predict=True,
        degree=1,
    )
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    ax3.plot(cleaned_dates, synthetic_inflation_values, marker='x', linestyle='--', color='red', markersize=4,
             label='Синтетичні дані')
    ax3.plot(cleaned_dates, synthetic_trend_values, linestyle='--', color='blue',
             label='Синтетичні тренд')
    ax3.set_xlabel("Дата")
    ax3.set_ylabel("Користувачі")
    plt.xticks(rotation=45)
    ax3.grid(True)
    plt.legend()
    plt.title("Графік користувачів (Синтетичний)")

    canvas3 = FigureCanvasTkAgg(fig3, master=frame3)
    canvas_widget3 = canvas3.get_tk_widget()
    canvas_widget3.pack()

    mse, rmse = evaluate_anomaly_detection_performance(values, cleaned_values)

    print(f"Середній квадратичний відхил (MSE): {mse}")
    print(f"Кореневий середній квадратичний відхил (RMSE): {rmse}")
    root.mainloop()
