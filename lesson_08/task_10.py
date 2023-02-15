import openpyxl

name = input('Name: ')
surname = input('Surname: ')
age = int(input('Age: '))

wb = openpyxl.Workbook()
sheet = wb.active

sheet['A1'] = 'Name'
sheet['B1'] = 'Surname'
sheet['C1'] = 'Gender'

sheet['A2'] = name
sheet['B2'] = surname
sheet['C2'] = age

wb.save('file_10.xlsx')
