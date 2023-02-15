class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_voice(self):
        print('Я не знаю какой звук мне издать, я же абстрактное животное')


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_voice(self):
        print('Гав')


class Cat(Animal):
    def __init__(self, name, age, is_vaccinated):
        super().__init__(name, age)
        self.is_vaccinated = is_vaccinated

    def make_voice(self):
        print('Мяу')


animals = [
    Animal('Животное', 5), # создание абстрактного животного довольно бессмысленно, но для понимания ООП это ок
    Dog('Шарик', 10, 'Доберман'),
    Cat('Матроскин', 9, True),
]
for animal in animals:
    animal.make_voice()
