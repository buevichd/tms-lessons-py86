from functools import reduce


def input_list(prompt='', sep=' ', element_type: type = int) -> list:
    return [element_type(s) for s in input(prompt).split(sep)]


numbers = input_list()

print(f'4.1: {reduce(lambda x, y: x + y, numbers)}')
print(f'4.2: {reduce(lambda x, y: min(x, y), numbers)}')
print(f'4.3: {reduce(lambda x, y: x * y, numbers)}')
print(f'4.4: {reduce(lambda x, y: x * y, range(1, 6))}')


# 4.5
def my_reduce(func, iterable, initial_value):
    result = initial_value
    for el in iterable:
        result = func(result, el)
    return result


print(f'4.5: {my_reduce(lambda x, y: x + y, numbers, 0)}')