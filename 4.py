from itertools import product

n = int(input("Введите число N: "))

# генерируем все возможные комбинации нулей и единиц длины n
combinations = list(product(['0', '1'], repeat=n))

# сортируем комбинации в лексикографическом порядке
combinations.sort()

# выводим все комбинации по одной в столбик
for combination in combinations:
    print(''.join(combination))