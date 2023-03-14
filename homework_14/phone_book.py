import sqlite3

DB_FILE = 'phone_db.sqlite'


def add_contact(name, phone):
    with sqlite3.connect(DB_FILE) as connection:
        data = (name, phone)
        connection.execute('INSERT INTO contact (name, phone) VALUES (?, ?)', data)


def print_all_contacts():
    with sqlite3.connect(DB_FILE) as connection:
        result = connection.execute('SELECT * FROM contact ORDER BY name')
        print(result.fetchall())


def update_contact(name, new_phone):
    with sqlite3.connect(DB_FILE) as connection:
        data = (new_phone, name)
        c = connection.execute('UPDATE contact SET phone = ? WHERE name = ?', data)


def main():
    while True:
        print('Введите номер операции:')
        print('0. Выйти из программы')
        print('1. Добавить новый контакт')
        print('2. Вывести весь список контактов в алфавитном порядке')
        print('3. Обновить номер контакта')
        operation = int(input())

        if operation == 0:
            print('Всего доброго!')
            break
        elif operation == 1:
            name = input('Имя контакта: ')
            phone = input('Номер контакта: ')
            add_contact(name, phone)
        elif operation == 2:
            print_all_contacts()
        elif operation == 3:
            name = input('Имя существующего контакта: ')
            new_phone = input('Новый номер контакта: ')
            update_contact(name, new_phone)
        else:
            print('Не поддерживаемая операция')


if __name__ == '__main__':
    main()
