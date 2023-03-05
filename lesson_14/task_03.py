import sqlite3


with sqlite3.connect('db.sqlite') as connection:
    all_users = connection.execute('SELECT * FROM user')
    for user in all_users.fetchall():
        print(user)

    min_age = int(input('Введите минимальный возраст: '))
    users = connection.execute(
        'SELECT * FROM user WHERE age >= ?;',
        (min_age,))
    for user in users.fetchall():
        print(user)
