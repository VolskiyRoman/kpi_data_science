import json
import statistics

# Відкриваємо файл JSON та завантажуємо його дані
with open('channels_data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

numbers_list = []
for channel_info in data.values():
    number = channel_info[2]  # Вибираємо третій елемент (індекс 2) з кожного списку
    numbers_list.append(number)

# Медіана
median_value = statistics.median(numbers_list)

# Середнє значення (математичне сподівання)
mean_value = statistics.mean(numbers_list)

# Дисперсія
variance_value = statistics.variance(numbers_list)

# Стандартне відхилення
stdev_value = statistics.stdev(numbers_list)

# Мода
mode_value = statistics.mode(numbers_list)

categories_count = {}
languages_count = {}
countries_count = {}

# Проходимося по кожному запису у файлі JSON
for channel_info in data.values():
    category = channel_info[4]  # Категорія - п'ятий елемент у списку
    language = channel_info[3]  # Мова - четвертий елемент у списку
    country = channel_info[5]   # Країна - шостий елемент у списку

    # Підраховуємо кількість кожної категорії, мови і країни
    if category in categories_count:
        categories_count[category] += 1
    else:
        categories_count[category] = 1

    if language in languages_count:
        languages_count[language] += 1
    else:
        languages_count[language] = 1

    if country in countries_count:
        countries_count[country] += 1
    else:
        countries_count[country] = 1

most_popular_category = max(categories_count, key=categories_count.get)
most_popular_language = max(languages_count, key=languages_count.get)
most_popular_country = max(countries_count, key=countries_count.get)

print("Медіана:", median_value)
print("Середнє значення:", mean_value)
print("Дисперсія:", variance_value)
print("Стандартне відхилення:", stdev_value)
print("Мода:", mode_value)
print("Найпопулярніша категорія:", most_popular_category)
print("Найпопулярніша мова:", most_popular_language)
print("Найпопулярніша країна:", most_popular_country)
