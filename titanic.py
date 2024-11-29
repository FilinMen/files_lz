import matplotlib.pyplot as plt
import pandas as pd

data_tit = pd.read_parquet('titanic.parquet', engine='pyarrow')
df = pd.DataFrame(data_tit)
print(df)
'''
df_letter['Количество'] = pd.to_numeric(df_letter['Количество'])

plt.figure(figsize=(10, 6))# Ширина фигуры будет 10 дюймов, а высота — 6 дюймов.
plt.bar(df_letter['Буквы'], df_letter['Количество'], color='skyblue')#plt.bar создает столбчатую диаграмму.
plt.xlabel('Буквы')#оси X, представляющие буквы
plt.ylabel('Количество')#оси Y, представляющие Количество
plt.title('Встречаемость букв в тексте')#plt.title задает заголовок для графика.
plt.grid(True)#plt.grid(True) включает отображение сетки на графике, что помогает лучше визуализировать данные.
plt.show()
'''PassengerId  Survived  Pclass  Name Sex   Age SibSp Parch Ticket Fare Cabin Embarked