import csv

# Функция для удаления "руб." и преобразования строки в число
def process_price(price_str):
    # Убираем "руб." и пробелы, затем преобразуем в число
    return float(price_str.replace('руб.', '').replace(' ', '').strip())

# Чтение и обработка данных из CSV файла
input_filename = "price.csv"
output_filename = "processed_price.csv"
processed_data = []

with open(input_filename, 'r', newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    headers = next(reader)  # Чтение заголовка
    for row in reader:
        # Обработка первой колонки (цены)
        processed_price = process_price(row[0])
        processed_data.append([processed_price])

# Запись обработанных данных в новый CSV файл
with open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(headers)  # Запись заголовка
    writer.writerows(processed_data)

print(f"Данные успешно обработаны и сохранены в {output_filename}")