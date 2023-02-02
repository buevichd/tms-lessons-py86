def filter_odd_numbers(numbers: list) -> list:
    result = []
    for num in numbers:
        if num % 2 == 0:
            # добавляем только чётные
            result.append(num)
    return result


print(filter_odd_numbers([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
print(filter_odd_numbers([7, 15, 32, 18, 5]))  # [32, 18]


# а можно в одну строчку, используя генератор списков :)
def filter_odd_numbers_with_generator(numbers: list) -> list:
    return [num for num in numbers if num % 2 == 0]


print(filter_odd_numbers_with_generator([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
print(filter_odd_numbers_with_generator([7, 15, 32, 18, 5]))  # [32, 18]