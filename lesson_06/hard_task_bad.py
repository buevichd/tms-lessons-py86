size = int(input())
matrix = []
for i in range(size):
    row = []
    for num in input().split():
        row.append(int(num))
    matrix.append(row)
main_diag_sum = 0
for i in range(size):
    main_diag_sum += matrix[i][i]
additional_diag_sum = 0
for i in range(size):
    additional_diag_sum += matrix[i][size - i - 1]
is_magic = main_diag_sum == additional_diag_sum
for i in range(size):
    row_sum = 0
    for j in range(size):
        row_sum += matrix[i][j]
    if row_sum != main_diag_sum:
        is_magic = False
        break
for j in range(size):
    col_sum = 0
    for i in range(size):
        col_sum += matrix[i][j]
    if col_sum != main_diag_sum:
        is_magic = False
        break
print(is_magic)
