# Пользователь вводит в консоли число секунд.
# Выведите число секунд в виде:
# 1. минуты:секунды

seconds = int(input())
minutes = seconds // 60
seconds %= 60
print(str(minutes) + ':' + str(seconds))



