import openpyxl

wb = openpyxl.load_workbook('file_10.xlsx')
sheet = wb.active
print(f'{sheet["A2"].value} {sheet["B2"].value} {sheet["C2"].value}')
