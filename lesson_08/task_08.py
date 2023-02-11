import csv

with open('file_07.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    passed_header = False
    for row in reader:
        if not passed_header:
            # Пропускаем первую строку, так как это названия столбцов
            passed_header = True
            continue

        print(f'{row[0]} {row[1]} {row[2]}')

        # А можно с помощью функции join()
        print(' '.join(row))

        # А можно с помощью функции format()
        print('{} {} {}'.format(*row))
