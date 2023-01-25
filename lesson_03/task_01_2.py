# Пользователь вводит в консоли число секунд.
# Выведите число секунд в виде:
# 2. дни:часы:минуты:секунды.

seconds = int(input())
days = seconds // (60 * 60 * 24)
hours = seconds % (60 * 60 * 24) // (60 * 60)
minutes = seconds % (60 * 60) // 60
seconds %= 60
print(str(days) + ':' + str(hours) + ':' + str(minutes) + ':' + str(seconds))



