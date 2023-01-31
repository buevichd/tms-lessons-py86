summa = 0
for i in range(101):
    summa += i
print(f'1: {summa}')


summa = 0
for i in range(100, 1001):
    summa += i
print(f'2: {summa}')


summa = 0
for i in range(100, 1001, 2):
    summa += i
print(f'3: {summa}')


factorial = 1
for i in range(2, 11):
    factorial *= i
print(f'4: {factorial}')


two_pow = 1
for i in range(10):
    two_pow *= 2
print(f'5: {two_pow}')


summa = 0
i = 0
while summa <= 1000:
    i += 1
    summa += i
print(f'6: {summa}')
