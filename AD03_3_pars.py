from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Инициализация драйвера
driver = webdriver.Chrome()

# URL страницы
url = "https://www.divan.ru/category/divany-i-kresla"
driver.get(url)

# Пауза для загрузки страницы (можно заменить на ожидание элементов)
time.sleep(5)

# Поиск элементов с ценами
prices = driver.find_elements(By.CLASS_NAME, 'lsooF')
print(prices)

# Список для хранения данных
parsed_data = []

# Вывод цен
for price in prices:
    data = price.find_element(By.CLASS_NAME, 'ui-LD-ZU').text  # Исправлено на find_element и By.CLASS_NAME
    parsed_data.append([data])
    print(parsed_data)

# Закрытие драйвера
driver.quit()

# Запись в CSV файл
with open("price.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])
    for row in parsed_data:
        writer.writerow(row)