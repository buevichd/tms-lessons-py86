import json

name = input('Name: ')
surname = input('Surname: ')
age = int(input('Age: '))

data = {'name': name, 'surname': surname, 'age': age}

with open('file_04.json', 'w') as file:
    json.dump(data, file, indent=2)
