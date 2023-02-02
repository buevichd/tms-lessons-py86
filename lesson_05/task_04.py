def my_round(num: float, digits: int = 0):
    ten_pow = 10 ** digits
    num *= ten_pow
    if num - int(num) < 0.5:
        num = int(num)
    else:
        num = int(num) + 1
    num /= ten_pow
    return num


print(my_round(10.4))  # 10.0
print(my_round(10.7))  # 11.0
print(my_round(12.51, 1))  # 12.5
print(my_round(12.55, 1))  # 12.6
print(my_round(12.753, 2))  # 12.75
print(my_round(12.759, 2))  # 12.76
