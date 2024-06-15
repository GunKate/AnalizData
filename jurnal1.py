import pandas as pd
import matplotlib.pyplot as plt

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

df = pd.DataFrame(data)
#print(df)

mean_subject = df.groupby('subject')['estimate'].mean()
print(mean_subject)

median_subject = df.groupby('subject')['estimate'].median()
print(median_subject)