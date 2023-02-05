def input_numbers_line() -> list[int]:
    return [int(num) for num in input().split()]


def input_matrix(size: int) -> list[list[int]]:
    return [input_numbers_line() for i in range(size)]


def calc_main_diag_sum(matrix: list[list[int]]) -> int:
    return sum(matrix[i][i] for i in range(len(matrix)))


def calc_additional_diag_sum(matrix: list[list[int]]) -> int:
    size = len(matrix)
    return sum(matrix[i][size - i - 1] for i in range(size))


def calc_row_sum(matrix: list[list[int]], row_index: int) -> int:
    return sum(matrix[row_index])


def calc_column_sum(matrix: list[list[int]], column_index: int) -> int:
    return sum(matrix[i][column_index] for i in range(len(matrix)))


def check_rows(matrix: list[list[int]], magic_sum: int):
    # Эта функция возвращает True если все строки матрицы в сумме дают magic_sum
    for i in range(len(matrix)):
        row_sum = calc_row_sum(matrix, i)
        if row_sum != magic_sum:
            return False
    return True


def check_columns(matrix: list[list[int]], magic_sum: int):
    # Эта функция возвращает True если все столбцы матрицы в сумме дают magic_sum
    # Её можно написать так же как check_rows, но также можно использовать
    # встроенную функцию all и написать всё в одну строку
    return all(calc_column_sum(matrix, i) == magic_sum for i in range(len(matrix)))


def is_magic(matrix: list[list[int]]) -> bool:
    magic_sum = calc_main_diag_sum(matrix)
    if magic_sum != calc_additional_diag_sum(matrix):
        return False
    return check_rows(matrix, magic_sum) and check_columns(matrix, magic_sum)


def main():
    size = int(input())
    matrix = input_matrix(size)
    print(is_magic(matrix))


if __name__ == '__main__':
    main()
