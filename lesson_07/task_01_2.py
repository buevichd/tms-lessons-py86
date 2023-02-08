def input_list(prompt='', sep=' ', element_type: type = int) -> list:
    return [element_type(s) for s in input(prompt).split(sep)]


lst = input_list(prompt='Введите числа с плавающей точкой через запятую: ', sep=',',
                 element_type=float)
print(lst)

# Пример работы:
# Введите числа с плавающей точкой через запятую: 1,2.5,-5.2
# [1.0, 2.5, -5.2]
