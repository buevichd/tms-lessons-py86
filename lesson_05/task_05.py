def get_natural_numbers(n: int) -> list:
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
    return numbers


print(get_natural_numbers(3))  # [1, 2, 3]
print(get_natural_numbers(5))  # [1, 2, 3, 4, 5]


# а можно было использовать генератор списков
def get_natural_numbers_with_generator(n: int) -> list:
    return [i for i in range(1, n + 1)]


print(get_natural_numbers_with_generator(3))  # [1, 2, 3]
print(get_natural_numbers_with_generator(5))  # [1, 2, 3, 4, 5]
