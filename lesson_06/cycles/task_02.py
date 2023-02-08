# Дан список чисел. Найти их сумму.

my_list = [7, 10, 13]

# а можно было запросить у пользователя ввести числа через пробел
# my_list = [int(i) for i in input().split()]

s = 0
for i in my_list:
    s += i
print(s)
