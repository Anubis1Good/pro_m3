import pandas as pd
df = pd.read_csv('googleplaystore.csv')
# Выведи на экран приложение с индексом 10472. Посмотри, какие ошибки допущены в значениях.
print(df.iloc[10472])
# Исправь ошибки, допущенные в значениях
columns = list(df.columns)
index = 10472
for i in range(len(columns) -1, 1, -1):
   df[columns[i]][index] = df[columns[i - 1]][index]


# Среди значений приложения стоит несколько пустых ('NaN'). Замени эти пустые значения на 'Lifestyle'.
df['Category'][index] = 'LIFESTYLE'
df['Genres'][index] = 'Lifestyle'


# Выведи на экран приложение, чтобы убедиться, что очистка прошла успешно
print(df.iloc[10472])
