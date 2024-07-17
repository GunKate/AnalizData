from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

# Настройка веб-драйвера
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Запуск в фоновом режиме
driver = webdriver.Chrome(options=options)

# Открытие страницы
url = 'https://www.divan.ru/category/stoly-pismennye-i-kompyuternye'
driver.get(url)

# Подождем немного, чтобы страница полностью загрузилась
time.sleep(5)

# Сбор данных о товарах
items = driver.find_elements(By.CLASS_NAME, 'wYUX2')

data = []

for item in items:
    name = item.find_element(By.CLASS_NAME, 'ui-GPFV8 qUioe ProductName ActiveProduct').text
    price = item.find_element(By.CLASS_NAME, 'ui-LD-ZU KIkOH').text
    data.append({
        'product': name,
        'price': price
    })

# Закрытие браузера
driver.quit()

# Сохранение данных в CSV файл
filename = 'prices.csv'

with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['product', 'price']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)

print(f"Данные успешно сохранены в файл {filename}")