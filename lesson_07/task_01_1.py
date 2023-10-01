# В этом файле показаны реализации функции input_list тремя способами
# Все варианты функции названы по разному просто для избежания коллизии имён

# с помощью обычного цикла
def input_list_with_simple_cycle() -> list[int]:
    input_strings = input().split()
    input_numbers = []
    for s in input_strings:
        input_numbers.append(int(s))
    return input_numbers


# с помощью генератора списков
def input_list_with_generator() -> list[int]:
    return [int(s) for s in input().split()]


# с помощью функции map
def input_list_with_map() -> list[int]:
    return list(map(int, input().split()))


print(input_list_with_simple_cycle())
print(input_list_with_generator())
print(input_list_with_map())
