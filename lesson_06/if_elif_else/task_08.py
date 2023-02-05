# Даны три числа, выведите максимальное из них (не используя функцию max
# и не создавая дополнительных переменных и сделав не более 2 сравнений
# для нахождения результата).

x = int(input())
y = int(input())
z = int(input())

# читерское решение
print(max(x, y, z))


# это уже не читерское решение, но возможное количество сравнений от 2 до 4
if x >= y and x >= z:
    print(x)
elif y >= x and y >= z:
    print(y)
else:
    print(z)


# Это решение предполагалось здесь, оно самое быстрое,
# так как при любых значениях x, y, z ему нужно всего 2 операции сравнения
if x >= y:
    if x >= z:
        print(x)
    else:
        print(z)
else:
    if y >= z:
        print(y)
    else:
        print(z)
