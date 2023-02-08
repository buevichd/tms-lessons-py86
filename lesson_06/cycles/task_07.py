# Дан словарь "слово" -> число.
# Вывести ключ, соответствующий максимальному значению.
# Пример: {'a': 1, 'b': 2} -> 'b'.

my_dict = {'a': 1, 'b': 5, 'c': 3}

# короткое, но сложное для понимания решение
print(max(my_dict.items(), key=lambda x: x[1])[0])

# решение через цикл и .items()
max_value = None
result_key = None
for key, value in my_dict.items():
    if max_value is None or value > max_value:
        max_value = value
        result_key = key

print(result_key)
