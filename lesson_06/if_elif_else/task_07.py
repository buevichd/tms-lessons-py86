# Дано три числа. Вывести количество положительных чисел среди них.

x = int(input())
y = int(input())
z = int(input())
positive_count = 0

if x > 0:
    positive_count += 1

if y > 0:
    positive_count += 1

if z > 0:
    positive_count += 1

print(positive_count)
