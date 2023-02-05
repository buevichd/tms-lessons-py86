# Дан словарь "слово" -> число.
# Вывести максимальное число среди значений словаря.
# Пример: {'a': 1, 'b': 2} -> 2.

my_dict = {'a': 1, 'b': 5, 'c': 3}

# читерское решение
print(max(my_dict.values()))

# решение через цикл и .items()
# Помечаем max_value как пустое значение
max_value = None
# вместо items() здесь можно было использовать .values(),
# но важно чтобы вы увидели синтаксис прохода по словарю: key, value
for key, value in my_dict.items():
    if max_value is None or value > max_value:
        max_value = value

print(max_value)
