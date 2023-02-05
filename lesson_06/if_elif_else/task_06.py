# Дан номер месяца (число от 1 до 12). Выведите пору года,
# которой этот месяц принадлежит: зима, весна, лето или осень.

n = int(input())
if n <= 2 or n == 12:
    print('winter')
elif n >= 3 and n <= 5:
    print('spring')
elif n >= 6 and n <= 8:
    print('summer')
else:
    print('autumn')
