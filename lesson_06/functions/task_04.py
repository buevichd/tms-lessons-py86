def compare(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0


print(compare(10, 20))  # -1
print(compare(20, 10))  # 1
print(compare(10, 10))  # 0
