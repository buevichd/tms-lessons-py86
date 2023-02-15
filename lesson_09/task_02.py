class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed


# создание объекта
my_dog = Dog('Шарик', 10, 'Доберман')

# вывод поля класса Dog
print(my_dog.breed)

# вывод полей класса, унаследованных от класса Animal
print(my_dog.name)
print(my_dog.age)
