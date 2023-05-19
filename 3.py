n = int(input("Введите количество строк: "))

# создаем массив строк
print("Введите: Имя Фамилию и возраст человека")
strings = []
for i in range(n):
    string = input().split()
    strings.append(string)

#сортируем строки по возрасту
sorted_strings = sorted(strings, key=lambda x: int(x[2]))

# выводим отсортированные строки
for string in sorted_strings:
    print(' '.join(string))