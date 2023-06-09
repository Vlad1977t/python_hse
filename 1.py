import pandas as pd

# создаем таблицу со студентами
data = {
    'Фамилия': ['Иванов', 'Петров', 'Сидоров', 'Козлов', 'Смирнова', 'Кузнецова', 'Николаева', 'Васильева'],
    'Имя': ['Иван', 'Петр', 'Сергей', 'Андрей', 'Елена', 'Ольга', 'Мария', 'Александра'],
    'Год рождения': [1998, 1999, 2000, 1997, 1998, 2001, 1999, 2002],
    'Оценка за экзамен': [5, 7, 8, 4, 7, 5, 8, 6]
}
df = pd.DataFrame(data)

# выводим фамилии и год рождения студентов с оценкой хорошо (8-10 баллов)
good_grades = df[df['Оценка за экзамен'].between(6, 7)]
print(good_grades[['Фамилия', 'Год рождения']])