from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Инициализация драйвера
driver = webdriver.Chrome()

url = "https://www.divan.ru/category/divany-i-kresla"
driver.get(url)

# Пауза для загрузки страницы (можно заменить на ожидание элементов)
time.sleep(5)

# Поиск элементов с ценами
prices = driver.find_elements(By.CLASS_NAME, 'lsooF')
print (prices)

# Вывод цен
for price in prices:
    data = price.find_elements(By.CSS_CLASS_NAME, 'ui-LD-ZU KIkOH').text
    parsed_data.append([data])
    print(parsed_data)

# Закрытие драйвера
driver.quit()
#
# with open("price.csv", 'w', newline='', encoding='utf-8') as file:
#   writer = csv.writer(file)
#   writer.writerow(['Price'])
#   writer.writerow(parsed_data)