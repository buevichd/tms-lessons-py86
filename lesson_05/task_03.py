def sum_and_max(*args) -> tuple:
    summ = 0
    max_element = args[0]
    for element in args:
        summ += element
        max_element = max(max_element, element)
    return summ, max_element


print(sum_and_max(1, 2, 3))  # (6, 3)
print(sum_and_max(5, 4))  # (9, 5)
print(sum_and_max(1, 50, 1))  # (52, 50)


# ниже показан читерский вариант решения :)
def sum_and_max_cheating(*args):
    return sum(args), max(args)


print(sum_and_max_cheating(1, 2, 3))  # (6, 3)
print(sum_and_max_cheating(5, 4))  # (9, 5)
print(sum_and_max_cheating(1, 50, 1))  # (52, 50)
