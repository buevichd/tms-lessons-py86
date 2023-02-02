def list_sum(l: list) -> int:
    summ = 0
    for element in l:
        summ += element
    return summ


my_list = [1, 2, 3]
print(list_sum(my_list))  # 6

print(list_sum([100, 200]))  # 300
