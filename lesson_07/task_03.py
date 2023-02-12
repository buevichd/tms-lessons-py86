def input_list(prompt='', sep=' ', element_type: type = int) -> list:
    return [element_type(s) for s in input(prompt).split(sep)]


numbers = input_list()

print(f'3.1: {list(filter(lambda x: x >= 0, numbers))}')
print(f'3.2: {list(filter(lambda x: x % 2 == 0, numbers))}')

positive_count = len(list(filter(lambda x: x > 0, numbers)))
zero_count = len(list(filter(lambda x: x == 0, numbers)))
negative_count = len(list(filter(lambda x: x < 0, numbers)))
print(f'3.3: pos={positive_count}, zeros={zero_count}, neg={negative_count}')


# 3.4
def my_filter(predicate, iterable):
    return [el for el in iterable if predicate(el)]


print(f'3.4: {my_filter(lambda x: x > 0, numbers)}')


# 3.5
def my_filter_gen(predicate, iterable):
    for el in iterable:
        if predicate(el):
            yield el


print(f'3.5(wrong usage): {my_filter_gen(lambda x: x > 0, numbers)}')
print(f'3.5: {list(my_filter_gen(lambda x: x > 0, numbers))}')
