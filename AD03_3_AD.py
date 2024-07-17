import csv
import numpy as np
import matplotlib.pyplot as plt

# Функция для чтения цен из CSV файла
def read_prices_from_csv(filename):
    prices = []
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Пропускаем заголовок
        for row in reader:
            prices.append(float(row[0]))  # Преобразуем цену в float и добавляем в список
    return prices

# Чтение цен из файла
input_filename = "processed_price.csv"
prices = read_prices_from_csv(input_filename)

# Вычисление средней цены
average_price = np.mean(prices)
print(f"Средняя цена: {average_price:.2f} руб.")

# Построение гистограммы
plt.hist(prices, bins=20, edgecolor='black')
plt.title('Распределение цен')
plt.xlabel('Цена (руб.)')
plt.ylabel('Количество товаров')
plt.axvline(average_price, color='r', linestyle='dashed', linewidth=1, label=f'Средняя цена: {average_price:.2f} руб.')
plt.legend()
plt.show()