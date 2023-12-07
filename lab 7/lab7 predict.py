import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Зчитування даних з файлу
file_path = 'Data_Set_3.xls'
df = pd.read_excel(file_path)

# Конвертація стовбця OrderDate в формат datetime
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Групування за місяцем та сумування продажів
monthly_sales = df.groupby(df['OrderDate'].dt.to_period("M"))['Total'].sum()

# Прогнозування продажів на наступні 5 місяців
last_month_sales = monthly_sales.iloc[-1]
growth_rate = 0.05  # Зростання на 5%
forecasted_months = pd.date_range(start=monthly_sales.index[-1].to_timestamp(), periods=6, freq='M')[1:]
forecasted_sales = last_month_sales * (1 + growth_rate) ** np.arange(1, 6)

# Створення DataFrame для прогнозованих продажів
forecasted_df = pd.DataFrame({
    'Month': forecasted_months,
    'Forecasted Sales': forecasted_sales
})

# Об'єднання фактичних та прогнозованих продаж
combined_df = pd.concat([monthly_sales.reset_index(), forecasted_df], ignore_index=True)

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(combined_df['Month'], combined_df['Forecasted Sales'], label='Forecasted Sales', marker='o', linestyle='solid', color='green')
plt.title('Monthly Sales Forecast')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.legend()
plt.xticks(rotation=45)
plt.show()
