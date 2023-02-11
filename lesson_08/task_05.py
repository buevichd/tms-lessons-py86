import json


with open('file_04.json', 'r') as file:
    data = json.load(file)
    name = data['name']
    surname = data['surname']
    age = int(data['age'])
    print(f'{name} {surname} {age}')


# А можно так, используя функцию format()
with open('file_04.json', 'r') as file:
    data = json.load(file)
    print('{name} {surname} {age}'.format(**data))
