import pandas as pd
import matplotlib.pyplot as plt

# Создание данных
data = {
    'name': ['Vasya', 'Vasya', 'Vasya', 'Vasya', 'Vasya',
             'Petya', 'Petya', 'Petya', 'Petya', 'Petya',
             'Ylia', 'Ylia', 'Ylia', 'Ylia', 'Ylia',
             'Serg', 'Serg', 'Serg', 'Serg', 'Serg',
             'Anne', 'Anne', 'Anne', 'Anne', 'Anne'],
    'subject': ['mat', 'leng', 'fisic', 'bio', 'chem',
                'mat', 'leng', 'fisic', 'bio', 'chem',
                'mat', 'leng', 'fisic', 'bio', 'chem',
                'mat', 'leng', 'fisic', 'bio', 'chem',
                'mat', 'leng', 'fisic', 'bio', 'chem'],
    'estimate': [4, 5, 4, 5, 3,
                 3, 4, 5, 3, 5,
                 5, 5, 5, 5, 5,
                 3, 4, 3, 3, 4,
                 4, 3, 5, 4, 4]
}

# Создание DataFrame из данных
df = pd.DataFrame(data)

# Вывод DataFrame для проверки (закомментировано)
# print(df)

# Расчет среднего значения оценок по каждому предмету
mean_subject = df.groupby('subject')['estimate'].mean()
print(f'среднее значение - {mean_subject}')

# Расчет медианного значения оценок по каждому предмету
median_subject = df.groupby('subject')['estimate'].median()
print(f'медианное значение - {median_subject}')

# Расчет первого и третьего квартилей для оценок по математике
Q1_math = df[df['subject'] == 'mat']['estimate'].quantile(0.25)
Q3_math = df[df['subject'] == 'mat']['estimate'].quantile(0.75)

# Расчет межквартильного размаха (IQR) для оценок по математике
IQR = Q3_math - Q1_math
print("межквартильного размаха (IQR): ", IQR)

# Расчет стандартного отклонения оценок по каждому предмету
std_subject = df.groupby('subject')['estimate'].std()
print("стандартное отклонение по предмету: ")
print(std_subject)