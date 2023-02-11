import csv


name = input('Name: ')
surname = input('Surname: ')
age = int(input('Age: '))


with open('file_07.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['name', 'surname', 'age'])
    writer.writerow([name, surname, age])


# А можно было так, но это менее удобно
with open('file_07.csv', 'w') as file:
    file.write('name,surname,age\n')
    file.write(name)
    file.write(',')
    file.write(surname)
    file.write(',')
    file.write(str(age))
    file.write('\n')


# Или так
with open('file_07.csv', 'w') as file:
    file.write('name,surname,age\n')
    file.write(f'{name},{surname},{age}\n')
