import csv


with open('file_06.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['name', 'surname', 'gender'])
    writer.writerow(['Dmitry', 'Buevich', 'M'])
