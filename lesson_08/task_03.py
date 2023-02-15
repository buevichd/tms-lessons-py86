import json

my_data = {'name': 'Dmitry', 'surname': 'Buevich', 'age': 26}

with open('file_03.json', 'w') as file:
    json.dump(my_data, file, indent=2)
