# Дан список чисел. Найти их максимальное среди них.

my_list = [1, 2, 100, 3]

# а можно было запросить у пользователя ввести числа через пробел
# my_list = [int(i) for i in input().split()]

# читерский способ решения:
print(max(my_list))

# пока счиатем что максимальный элемент - это первый
max_element = my_list[0]
for i in my_list:
    # если текущий элемент больше max_element
    if i > max_element:
        # обновляем max_element
        max_element = i

print(max_element)
