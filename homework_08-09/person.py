import datetime


class Person:
    def __init__(self, full_name, age, gender):
        self.full_name = full_name
        self.age = age
        self.gender = gender

    def print_person_info(self):
        print(f"Person: {self.full_name} ({self.gender}), {self.age} years old")

    def get_birth_year(self):
        return datetime.datetime.now().year - self.age


if __name__ == '__main__':
    p = Person(' ')