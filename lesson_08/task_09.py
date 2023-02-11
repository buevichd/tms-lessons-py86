import openpyxl


wb = openpyxl.Workbook()
sheet = wb.active

sheet['A1'] = 'Name'
sheet['B1'] = 'Surname'
sheet['C1'] = 'Gender'

sheet['A2'] = 'Dmitry'
sheet['B2'] = 'Buevich'
sheet['C2'] = 'M'

wb.save('file_09.xlsx')
