# Дан список чисел. Если среди них есть ноль - вывести yes, иначе no.

my_list = [1, 2, 100, 0, 3]

# а можно было запросить у пользователя ввести числа через пробел
# my_list = [int(i) for i in input().split()]

has_zero = False
for i in my_list:
    if i == 0:
        has_zero = True
        break

if has_zero:
    print('yes')
else:
    print('no')
