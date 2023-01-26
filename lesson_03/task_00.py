# Напишите программу, которая спрашивает у пользователя как его зовут,
# затем какого он года рождения.
# После этого программа выводит Hello {name}. Your age is {age}.

name = input('What is your name? ')
year_of_birth = int(input('What your your year of birth? '))
age = 2023 - year_of_birth
print('Hello ' + name + '. Your age is ' + str(age))
