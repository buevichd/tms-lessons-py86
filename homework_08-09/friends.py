from person import Person

friends = [
    Person('Ivan', 20, 'M'),
    Person('Ivan', 21, 'M'),
    Person('Ivanka', 22, 'F'),
    Person('Ivanka', 19, 'F'),
]

for f in friends:
    f.print_person_info()


def get_oldest_person(fs):
    winner = fs[0]
    for f in fs:
        if f.age > winner:
            winner = f
    return winner


oldest_friend = get_oldest_person(friends)
oldest_friend.print_person_info()

male_friends = [f for f in friends if f.gender == 'M']
