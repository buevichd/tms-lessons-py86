def hello_world():
    print('Hello world!')


def my_sum(x, y):
    return x + y


def simple_compare(x, y):
    return x < y


def compare(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0


def filter_negative_numbers(numbers):
    new_numbers = []
    for num in numbers:
        if num >= 0:
            new_numbers.append(num)
    return new_numbers


n = int(input('Введите номер задачи: '))
if n == 1:
    hello_world()
elif n == 2:
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))
    result = my_sum(x, y)
    print(f'Сумма чисел: {result}')
elif n == 3:
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))
    result = simple_compare(x, y)
    print(f'Первое число меньше второго? Ответ: {result}')
elif n == 4:
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))
    result = compare(x, y)
    print(f'Результат сравнения: {result}')
elif n == 5:
    user_input = input('Введите числа, разделённые пробелом: ')
    numbers = []
    for num in user_input.split():
        numbers.append(int(num))
    filtered_numbers = filter_negative_numbers(numbers)
    print(f'Удалили отрицательные числа из вашего списка: {filtered_numbers}')
else:
    print('Задачи с таким номером нет.')


# Примечание.
# Вы возможно заметили, что код с вводом двух чисел повторяется в трёх местах программы.
# Это отличный повод чтобы вынести его в отдельную функцию.
# Также ввод пользователем списка чисел выглядит как то, что можно оформить как
# отдельную функцию и возможно переиспользовать в будущем.
# Тогда программа будет выглядеть так:
def input_two_numbers():
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))
    # Функция возвращает кортеж, скобки для создания кортежа можно опустить.
    # Запись return x, y аналогична записи return (x, y)
    return x, y


def input_numbers_list():
    user_input = input('Введите числа, разделённые пробелом: ')
    # вместо цикла здесь можно использовать генератор
    return [int(num) for num in user_input.split()]


n = int(input('Введите номер задачи: '))
if n == 1:
    hello_world()
elif n == 2:
    # вспоминаем тему "формы операторов присваивания
    # слева от знака равенства кортеж из двух элементов
    # справа от знака равенства - вызов функции, которая возвращает кортеж из 2 элементов
    x, y = input_two_numbers()
    result = my_sum(x, y)
    print(f'Сумма чисел: {result}')
elif n == 3:
    x, y = input_two_numbers()
    result = simple_compare(x, y)
    print(f'Первое число меньше второго? Ответ: {result}')
elif n == 4:
    x, y = input_two_numbers()
    result = compare(x, y)
    print(f'Результат сравнения: {result}')
elif n == 5:
    numbers = input_numbers_list()
    filtered_numbers = filter_negative_numbers(numbers)
    print(f'Удалили отрицательные числа из вашего списка: {filtered_numbers}')
else:
    print('Задачи с таким номером нет.')
