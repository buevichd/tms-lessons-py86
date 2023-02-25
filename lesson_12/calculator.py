def input_int_number() -> int:
    while True:
        try:
            return int(input('Введите целое число: '))
        except ValueError as e:
            print('Ошибка:', e)
            print('Попробуйте снова.')


class CalculationExitException(Exception):
    pass


def calculate(left: int, right: int, operation: str):
    if operation == '+':
        return left + right
    elif operation == '-':
        return left - right
    elif operation == '*':
        return left * right
    elif operation == '/':
        return left / right
    elif operation == '!':
        raise CalculationExitException()
    else:
        raise ValueError(f'Неподдерживаемая операция: {operation}')


def main():
    while True:
        try:
            left = input_int_number()
            right = input_int_number()
            operation = input('Введите операцию (введите ! для выхода из программы): ')
            result = calculate(left, right, operation)
            print('Результат операции:', result, end='\n\n')
        except ValueError as e:
            print('Ошибка:', e, end='\n\n')
        except ZeroDivisionError as e:
            print('Ошибка:', e, end='\n\n')
        except CalculationExitException:
            print('Завершаем программу')
            break


if __name__ == '__main__':
    main()
