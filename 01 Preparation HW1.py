# Описание задания: Посчитайте распределение тематик новостей в файле URL.txt (то есть какое количество раз
# встречается страница с каждой темой).Тематикой можно считать первое слово между знаками '/' в URL новости.

import re
# Загружаем файл целиком (получаем большую строку)
input_filename = r"C:\Users\MSI-PC\Desktop\NETOLOGY DS\ДЗ\01. Подготовка\ДЗ1/urls.txt"
input_file = open(input_filename)
input_data = input_file.read()

# Задаём паттерн для поиска и находим все совпадения в выгруженной из файла строке
pattern = r"/[a-z]+/"
news_headlines = re.findall(pattern, input_data)

# Создаём словарь и загружаем в него заголовки новостей с количеством повторений
stats = {}
for headline in news_headlines:
    stats.setdefault(headline, 0)
    stats[headline] += 1

for key in stats:
    print(key,":", stats[key])


