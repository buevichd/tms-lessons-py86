# Дана строка. Посчитайте сколько раз в ней встречается символ "a".

s = input()

count = 0
for char in s:
    if char == 'a':
        count += 1

print(count)
