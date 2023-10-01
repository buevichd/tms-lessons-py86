def input_list(prompt='', sep=' ', element_type: type = int) -> list:
    return [element_type(s) for s in input(prompt).split(sep)]


numbers = input_list()

print(f'2.1: {list(map(lambda x: x * 100, numbers))}')
print(f'2.2: {list(map(str, numbers))}')
print(f'2.3: {list(map(lambda x: round(x / 100), numbers))}')


# 2.4
def my_map(func, iterable):
    return [func(el) for el in iterable]


print(f'2.4: {my_map(str, numbers)}')


# 2.5
def my_map_gen(func, iterable):
    for el in iterable:
        yield func(el)


print(f'2.5(wrong usage): {my_map_gen(str, numbers)}')
print(f'2.5: {list(my_map_gen(str, numbers))}')
