
my_sum_lambda = lambda x, y: x + y

print(my_sum_lambda(1, 2))  # 3
print(my_sum_lambda(5, 5))  # 10



students_list = [
    ('Ivan', 'Ivanov', 2003),
    ('Petr', 'Petrov', 2005),
    ('Sidr', 'Sidorov', 2004)
]

# отсортируем студентов по фамилии
def get_surname(student: tuple) -> str:
    return student[1]

sorted_list = sorted(students_list, key=get_surname)


students_list = [
    ('Ivan', 'Ivanov', 2003),
    ('Petr', 'Petrov', 2005),
    ('Sidr', 'Sidorov', 2004)
]

# отсортируем студентов по фамилии с помощью lambda функции
sorted_list = sorted(students_list, key=lambda student: student[1])


numbers = [1, 2, 3]

# обычный подход
squared_nubmers = []
for num in numbers:
    squared_nubmers.append(num ** 2)

# подход с использованием генерторов списков
squared_nubmers = [num ** 2 for num in numbers]

# подход с ипользование функции map
squared_nubmers = list(map(lambda num: num ** 2, numbers))


numbers = [1, 2, 3, 4, 5, 6]

# обычный подход
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        # добавляем в результат только чётные числа
        even_numbers.append(num)

# подход с использованием генерторов списков
even_numbers = [num for num in numbers if num % 2 == 0]

# подход с ипользование функции filter
even_numbers = list(filter(lambda num: num % 2 == 0, numbers))


from functools import reduce

numbers = [2, 3, 4, 5]

# обычный подход
result = 1
for num in numbers:
    result *= num

# подход с ипользование функции reduce
result = reduce(lambda x, y: x * y, numbers, 1)


def my_decorator(original_func):
    def updated_func():
        print('Я код, отрабатывающий до вызова функции.')
        original_func()
        print('Я код, отрабатывающий после вызова функции')

    return updated_func

@my_decorator
def my_func():
    print('Я функция, которая не хочет, чтобы её код меняли.')

my_func()
# Я код, отрабатывающий до вызова функции.
# Я функция, которая не хочет, чтобы её код меняли.
# Я код, отрабатывающий после вызова функции


def wrap_in_transaction(f):
    return f


@wrap_in_transaction
def transfer_money(from_card, to_card, amount):
    # do some operations
    pass




def my_super_function(a: int, b: str) -> bool:
    """
    Это документация для моей функции my_super_function.
    Она записывается в самом начале функции, и обрамлена в три пары кавычек.
    По сути это просто многострочный комментарий.

    :param a: описание первого параметра функции.
    :param b: описание второго параметра функции.
    :return: подробное описание того, что эта функция возвращает
    """
    print("Do my super function...")



def my_decorator(func):
    def new_func(*args, **kwargs):
        print(f'Функция получила на вход значение {args} {kwargs}')
        result = func(*args, **kwargs)
        print(f'Результат функции: {result}')
        return result

    return new_func


@my_decorator
def my_func(a, b, c, d):
    return a + b + c + d

y = my_func(1, 2, d=3, c=4)
print(f'y = {y}')



f = open('my_file.txt', 'r')

print(f.read(1))
# H

print(f.read(3))
# ell

print(f.read())
# o this is just a text file
# This is second line


f = open('my_file.txt', 'r')

for line in f:
    print(line)

# Hello this is just a text file
#
# This is second line
#


f = open('my_file1.txt', 'w')

f.write('First line\n')
f.write('Second line\n')


# ключевое слово with используется для создания контекстного мернеджера
with open('my_file.txt', 'w') as f:
    f.write('Работаю с переменной f внутри блока с отступом\n')
    f.write('После конца блока будут освобождены все ресурсы\n')
    f.write('И переменной f уже нельзя будет пользоваться\n')

print('Блок контекстного менеджера закончен, ресурсы освобождены')


# 1
fs = []
for i in range(100000):
    fs.append(open('my_file.txt'))


# 2
for i in range(100000):
    f = open('my_file.txt')


# 1
import math
print(math.sin(math.pi / 2))

# 2
from math import sin, pi
print(sin(pi / 2))

# 3
from math import *
print(sin(pi / 2))


import csv

header = ('name', 'surname', 'gender')
students = [
    ('Ivan', 'Ivanov', 'M'),
    ('Petr', 'Petrov', 'M'),
    ('Victoria', 'Sidorova', 'F'),
]

with open('students.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(header)
    for student in students:
        writer.writerow(student)



import csv

with open('students.csv', 'r') as file:
    file_reader = csv.reader(file, delimiter=',')
    index = 0
    for row in file_reader:
        if index == 0:
            print(f'Названия столбцов: {row}')
        else:
            print(f'Строка со значенями: {row}')
        index += 1


import openpyxl

wb = openpyxl.Workbook()

sheet = wb.active
sheet['A1'] = 'Name'
sheet['B1'] = 'Surname'
sheet['A2'] = 'Dmitry'
sheet['B2'] = 'Buevich'

wb.save('workbook.xlsx')



class Employee:
   def __init__(self, employee_name, employee_age):
       self.name = employee_name  # поле "name"
       self.age = employee_age  # поле "age"

   # метод "Сделай отчёт"
   def make_report(self):
       print(self.name + ' делает отчёт...')


# создание объекта (экземпляра класса)
manager = Employee('Иван Иванов', 30)
manager.make_report()  # Иван Иванов делает отчёт...



class Square(Figure):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

a = Square(10)
b = Circle(5)
print(a.area(), b.area())



class Person:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, role):
        self.role = role

class Teacher(Person, Employee):
    def __init__(self, name):
        Person.__init__(self, name)
        Employee.__init__(self, 'Teacher')

t = Teacher('John')
print(t.name)
print(t.role)


class Human:
    @classmethod
    def get_kind(cls):
        return 'Homosapiens'

print(Human.get_kind())

oleg = Human()
print(oleg.get_kind())



class Human:
    @staticmethod
    def get_kind():
        return 'Homosapiens'

print(Human.get_kind())

oleg = Human()
print(oleg.get_kind())




class MyNumber:
    def __init__(self, number):
        self.number = number

    def plus(self, other):
        return MyNumber(self.number + other.number)

    def minus(self, other):
        return MyNumber(self.number - other.number)

    def mult(self, other):
        return MyNumber(self.number * other.number)

    def divide(self, other):
        return MyNumber(self.number / other.number)


a = MyNumber(1)
b = MyNumber(2)
c = MyNumber(3)
d = a.plus(b).minus(c).mult(a).divide(b)
print(d.number)




from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'

if __name__ == '__main__':
    app.run(port=8080, debug=True)




class MyNumber:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return MyNumber(self.number + other.number)

    def __sub__(self, other):
        return MyNumber(self.number - other.number)

    def __mul__(self, other):
        return MyNumber(self.number * other.number)

    def __truediv__(self, other):
        return MyNumber(self.number / other.number)


a = MyNumber(1)
b = MyNumber(2)
c = MyNumber(3)
d = a + b - c * a / b
print(d.number)




class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def distance_to_zero(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


point = Point(3, 4)
dist = point.distance_to_zero  # круглые скобки не нужны!
print(dist)



class Parent:
    def do_something(self):
        print('Parent method')

class Child(Parent):
    def do_something(self):
        print('Child method')

c = Child()
c.do_something()
# Child method



class Parent:
    def do_something(self):
        print('Parent method')


class Child(Parent):
    def do_something(self):
        super().do_something()
        print('Child method')


c = Child()
c.do_something()
# Parent method
# Child Method



class CreditCard:
    def __init__(self, card_holder, card_number):
        self.card_holder = card_holder
        self.card_number = card_number



from dataclasses import dataclass

@dataclass
class CreditCard:
    card_holder: str
    card_number: str




class Math:
    pi = 3.14

print(Math.pi)

math = Math()
print(math.pi)




def f1():
    print(1 / 0)

def f2():
    f1()

def f3():
    f2()

f3()



try:
    print(1 / 0)
except ZeroDivisionError as e:
    print('Исключение поймано:', e)
    # Исключение поймано: division by zero



try:
    a, b = int(input()), int(input())
    print(a / b)
except ZeroDivisionError as e:
    print('Исключение поймано:', e)
except ValueError as e:
    print('Некорректные данные:', e)
    # Некорректные данные: invalid literal for int() with base 10: 'qwerty'


try:
    a, b = int(input()), int(input())
    print(a / b)
except Exception as e:
    print('Сюда попадут ВСЕ исключения')
except ValueError as e:
    print('Мы никогда не попадём в этот блок')




try:
    a, b = int(input()), int(input())
    print(a / b)
except ZeroDivisionError as e:
    print('Исключение поймано:', e)
except ValueError as e:
    print('Некорректные данные:', e)
else:
    print('Программа завершилась без ошибок')




try:
    a, b = int(input()), int(input())
    print(a / b)
except ZeroDivisionError as e:
    print('Исключение поймано:', e)
except ValueError as e:
    print('Некорректные данные:', e)
finally:
    print('Вы прекрасны!')




def func():
    try:
        a, b = int(input()), int(input())
        return a / b
    except ZeroDivisionError as e:
        print('Исключение споймано:', e)
    except ValueError as e:
        print('Некорректные данные:', e)
    finally:
        print('Вы прекрасны!')

print(func())



num = int(input('Введите число больше нуля: '))
if num <= 0:
    raise ValueError('Ожидалось положительное число')





class PositiveNumberException(ValueError):
    pass

num = int(input('Введите число больше нуля: '))
if num <= 0:
    raise PositiveNumberException('Ожидалось положительное число')



l = [1, 2]
i = iter(l)
print(next(i))
print(next(i))
print(next(i))




class NaturalNumberIterator:
    """
    Итератор по первым `count` натуральным числам
    """
    def __init__(self, count):
        self.count = count
        self.current_number = 0

    def __next__(self):
        self.current_number += 1
        if self.current_number > self.count:
            raise StopIteration()
        return self.current_number

i = NaturalNumberIterator(3)
print(next(i))
print(next(i))
print(next(i))
print(next(i))




class NaturalNumberIterable:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return NaturalNumberIterator(self.count)


for i in NaturalNumberIterable(3):
    print(i)




class NaturalNumberIterable:
    def __init__(self, count):
        self.count = count
        self.current_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current_number += 1
        if self.current_number > self.count:
            raise StopIteration()
        return self.current_number


for i in NaturalNumberIterable(3):
    print(i)





import sys
import time

start = time.time()
lst = [i for i in range(100000000)]
print(time.time() - start)
print(sys.getsizeof(lst))




def my_range(start, finish):
    num = start
    while num < finish:
        yield num
        num += 1

for i in my_range(0, 100000000):
    print(i)




def my_range(start, finish):
    num = start
    while num < finish:
        print("Сейчас будет yield")
        yield num
        num += 1

for i in my_range(0, 5):
    print(i)




from flask import Flask, request

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    name = request.args.get('name', 'World')
    return f'<p>Hello, {name}!</p>'


if __name__ == '__main__':
    app.run(port=8080, debug=True)



app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return f'<p>Hello, World!</p>'


@app.route('/article/<int:id>')
def article_view(id: int):
    # use id to get article
    pass






from flask import Flask, request

app = Flask(__name__)

@app.route('/auth', methods=['POST'])
def authenticate():
    login = request.form['login']
    password = request.form['password']
    # handle authentication...





from flask import Flask, session, redirect
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/auth', methods=['POST'])
def authenticate():
    login = request.form['login']
    password = request.form['password']
    if check_user(login, password):
        session['is_authenticated'] = True
    return '<p>Some HTML</p>'

@app.route('/some/page')
def some_page():
    if session.get('is_authenticated', False):
        # return some html page...
        pass
    else:
        # redirect to login page
        return redirect('/auth')




from flask import Flask, session, abort

app = Flask(__name__)

@app.route('/article/<int:article_id>')
def article_page(article_id: int):
    article = get_article(article_id)
    if article is None:
        abort(404, 'Article not found')

    # handle request if everything OK
    return '<p>Some HTML</p>'





from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    like_count = models.IntegerField(default=0)





from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django! This is polls app.")





from django.shortcuts import render

def hello(request):
    data = {'name': 'Dmitry'}
    return render(request, 'prev/index.html', data)





# Запрос всех объектов
Question.objects.all()

# Запрос одного конкретного объекта
# Если такого объекта не найдётся, или найдётся более одного -
# будет выброшено исключение polls.models.Question.DoesNotExist
Question.objects.get(pk=1)
Question.objects.get(id=1)
Question.objects.get(question_text='Do you like Django?')


# Фильтрация объектов, поиск по параметрам
Choice.objects.filter(votes=0)
Choice.objects.exclude(votes=0)

# Подсчёт, сортировка
query_set = Choice.objects.filter(votes=0)
query_set.exists()
query_set.count()
query_set.order_by('-choice_text')
query_set.order_by('choice_text').reverse()


# Фильтрация по значениям текстовых полей
Question.objects.filter(question_text__exact='Do you like Django?')
Question.objects.filter(question_text__iexact='do you like django?')
Question.objects.filter(question_text__contains='Django')
Question.objects.filter(question_text__icontains='django')
Question.objects.filter(question_text__startswith='Do')
Question.objects.filter(question_text__istartswith='do')
Question.objects.filter(question_text__endswith='Django?')
Question.objects.filter(question_text__iendswith='django?')


# Фильтрация по значениям сравниваемых полей
Choice.objects.filter(votes__gt=0)
Choice.objects.filter(votes__gte=1)
Choice.objects.filter(votes__lt=5)
Choice.objects.filter(votes__lte=4)
Choice.objects.filter(id__in=[1, 3, 5])
Question.objects.filter(pub_date__lt=timezone.datetime.now())


# Фильтрация по связанным объектам
q = Question.objects.get(pk=1)
Choice.objects.filter(question=q)

Choice.objects.filter(question__id=1)
Choice.objects.filter(question__question_text='Do you like Django?')
Choice.objects.filter(question__question_text__icontains='django')


# Filters chain
Choice.objects \
    .filter(question__question_text__icontains='django') \
    .filter(votes__gt=0) \
    .exclude(question__pub_date__gt=timezone.datetime.now()) \
    .order_by('choice_text') \
    .reverse()


# Фильтрация с условием AND
Choice.objects.filter(votes__gte=5, votes__lt=10)
Choice.objects.filter(votes__gte=5).filter(votes__lt=10)

# Фильтрация с условием OR и NOT
from django.db.models import Q
Choice.objects.filter(Q(votes__gt=5) | ~Q(choice_text='Yes'))

# Комбинация фильтров как переменная
filters = Q(votes__gt=5) | Q(votes=0)
filters &= Q(choice_text='Yes')
Choice.objects.filter(filters)


from django.db.models import Count, Sum, Max

# Аннотации (создание "временных" полей)
query_set = Question.objects.annotate(choice_count=Count('choices'))
query_set.filter(choice_count__gt=0)

# Агрегация данных
Choice.objects.aggregate(sum_vote_count=Sum('votes'))


# Фильтрация с условием AND
Choice.objects.filter(votes__gte=5, votes__lt=10)
Choice.objects.filter(votes__gte=5).filter(votes__lt=10)

# Фильтрация с условием OR и NOT
from django.db.models import Q
Choice.objects.filter(Q(votes__gt=5) | ~Q(choice_text='Yes'))

# Комбинация фильтров как переменная
filters = Q(votes__gt=5) | Q(votes=0)
filters &= Q(choice_text='Yes')
Choice.objects.filter(filters)




from django.db.models import Count, Sum, Max

# Аннотация (создание) временно поля "choice_count"
Question.objects \
    .annotate(choice_count=Count('choices')) \
    .filter(choice_count__gt=0)

# Подсчёт суммарного количества голосов
Choice.objects.aggregate(total_votes_count=Sum('votes'))
# {'total_votes_count': 123}

# Аннотация временного поля + подсчёт максимального значения
Question.objects \
    .annotate(choice_count=Count('choices')) \
    .aggregate(max_choice_count=Max('choice_count'))
# {'max_choice_count': 15}




class MyModel(models.Model):
    my_field_1 = models.CharField(max_length=100)
    my_field_2 = models.IntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['my_field_1', '-my_field_2'])
        ]


class BankAccount(models.Model):
    money = models.FloatField(default=0.0)


class CarCompany(models.Model):
    name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=3)


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    car_company = models.OneToOneField(CarCompany,
                                       related_name='car_model',
                                       on_delete=models.CASCADE)


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Subject(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='subjects')








class BaseUser(models.Model):
    username = models.CharField(max_length=100)
    
    class Meta:
        abstract = True
        
        
class Manager(BaseUser):
    project = models.CharField(max_length=100)
    
    
class Engineer(BaseUser):
    language = models.CharField(max_length=100)






from polls.models import Question, Choice
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    choices = serializers.HyperlinkedRelatedField(
        view_name='choice-detail',
        read_only=True,
        many=True,
    )

    class Meta:
        model = Question
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    question = serializers.HyperlinkedRelatedField(
        view_name='question-detail',
        read_only=True
    )

    class Meta:
        model = Choice
        fields = '__all__'






from polls.models import Question


q1, q2 = Question.objects.bulk_create([
    Question(question_text='How are you?', pub_date=timezone.now()),
    Question(question_text='Do you like Django?', pub_date=timezone.now()),
])

q1.question_text = 'Updated Text 1'
q2.question_text = 'Updated Text 2'
Question.objects.bulk_update([q1, q2], ['question_text'])






from rest_framework import viewsets

from polls.models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer







from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('questions', views.QuestionViewSet)
router.register('choices', views.ChoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]






def index(request):
    lang = request.COOKIES.get('preferable_language', 'en')
    # use language
    context = {'questions': Question.objects.all()}
    response = render(request, 'polls/index.html', context)
    response.set_cookie('preferable_language', lang)
    return response






class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.prefetch_related('choices')
    serializer_class = QuestionSerializer
    # список бекенд фильтров, используемых для кастомизации эндпоинта
    filter_backends = [filters.OrderingFilter]
    # ordering_fields - необязательное поле, которое ограничивает
    # поля, по которым можно сортировать
    ordering_fields = ['id', 'question_text', 'pub_date']






from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def test_view(request):
    my_param_1 = request.query_params.get('my_param_1')
    my_param_2 = request.query_params.get('my_param_2')
    data = {'status': 'ok', 'param_values': [my_param_1, my_param_2]}
    return Response(data)





from django.contrib.auth.models import User

user = User.objects.create_user(username="johnlennon",
                                email="lennon@thebeatles.com",
                                password="johnpassword")
user.first_name = 'John'
user.last_name = 'Lennon'
user.save()





user = User.objects.get(username='johnlennon')
# user.password = 'newpassword'  # не будет работать
user.set_password('newpassword')
user.save()
    





from django.contrib.auth import authenticate

user = authenticate(username="johnlennon", password="johnpassword")
if user is not None:
    # A backend authenticated the credentials
    ...
else:
    # No backend authenticated the credentials
    ...







from django.contrib.auth import authenticate, login


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...






from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    # Redirect to a success page.





def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(f'/accounts/login?next={request.path}')
    ...






from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    ...




CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "127.0.0.1:11211",
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "/var/tmp/django_cache",
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "my_cache_table",
    }
}


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}





MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    ...,
    'django.middleware.cache.FetchFromCacheMiddleware',
]





from django.core.cache import cache

cache.set('my_key', 'hello, world!', 30)
print(cache.get('my_key'))  # hello, world! 





import time

def f1():
    print('f1 started')
    time.sleep(2)
    print('f1 finished')

def f2():
    print('f2 started')
    time.sleep(2)
    print('f2 finished')

def main():
    f1()
    f2()

start_time = time.time()
main()
end_time = time.time()
print(f'Total time: {end_time - start_time}s')





import time
import asyncio

async def f1():
    print('f1 started')
    await asyncio.sleep(2)
    print('f1 finished')

async def f2():
    print('f2 started')
    await asyncio.sleep(2)
    print('f2 finished')

async def main():
    task1 = asyncio.create_task(f1())
    task2 = asyncio.create_task(f2())
    await task1
    await task2

start_time = time.time()
asyncio.run(main())
end_time = time.time()
print(f'Total time: {end_time - start_time}s')





import time

def f1():
    print('f1 started')
    time.sleep(2)
    print('f1 finished')

print(type(f1))
print(type(f1()))




import asyncio

async def f1():
    print('f1 started')
    await asyncio.sleep(2)
    print('f1 finished')

print(type(f1))
print(type(f1()))



import asyncio

async def f1():
    print('f1 started')
    await asyncio.sleep(2)
    print('f1 finished')

async def main():
    task = asyncio.create_task(f1())
    print(type(task))
    print(task.__class__.__bases__)
    await task

asyncio.run(main())






import asyncio
import time

async def f1():
    print('f1 started')
    await asyncio.sleep(2)
    print('f1 finished')

async def f2():
    print('f2 started')
    await asyncio.sleep(2)
    print('f2 finished')

async def main():
    await f1()
    await f2()

start_time = time.time()
asyncio.run(main())
end_time = time.time()
print(f'Total time: {end_time - start_time}s')





import requests
import time


cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
          'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']


start_time = time.time()
for city in cities:
    url = 'https://api.openweathermap.org/data/2.5/weather' \
          f'?appid=2a4ff86f9aaa70041ec8e82db64abf56&q={city}&units=metric'

    temp = requests.get(url).json()['main']['temp']

    print(f'Temperature in {city}: {temp}')

end_time = time.time()
print(f'Work time: {end_time - start_time}')







import asyncio
import time

import aiohttp


cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
          'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']


async def get_weather(city):
    url = 'https://api.openweathermap.org/data/2.5/weather' \
          f'?appid=2a4ff86f9aaa70041ec8e82db64abf56&q={city}&units=metric'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            temp = data['main']['temp']
            print(f'Temperature in {city}: {temp}')


async def main():
    tasks = []
    for city in cities:
        tasks.append(asyncio.create_task(get_weather(city)))
    await asyncio.gather(*tasks)


start_time = time.time()
asyncio.run(main())
end_time = time.time()
print(f'Work time: {end_time - start_time}')





import os
from telegram import Update
from telegram.ext import CallbackContext, ApplicationBuilder, CommandHandler

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(f'Hello {update.effective_user.full_name}!')

if __name__ == '__main__':
    token = os.environ['TELEGRAM_BOT_TOKEN']
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler('start', start))
    app.run_polling()






import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

async def start(update: Update, context: CallbackContext):
    await update.message.reply_html(rf"Hi {update.effective_user.mention_html()}!")

async def help(update: Update, context: CallbackContext):
    await update.message.reply_html("There should be help message")

async def echo(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(update.message.text)

if __name__ == "__main__":
    application = Application.builder().token(os.environ['TELEGRAM_BOT_TOKEN']).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling()




import os

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

DB_PATH = os.path.abspath('db.sqlite3')
engine = create_engine(f'sqlite:////{DB_PATH}', echo=True)
if not database_exists(engine.url):
    create_database(engine.url)




from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100))
    password = Column(String(100))





from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    ...

    address = relationship('Address', back_populates='user', uselist=False)


class Address(Base):
    __tablename__ = 'address'
    ...

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='address', uselist=False)




class Order(Base):
    __tablename__ = 'order'
    ...

    order_entries = relationship('OrderEntry', back_populates='order')


class OrderEntry(Base):
    __tablename__ = 'order_entry'
    id = Column(Integer, primary_key=True, autoincrement=True)
    count = Column(Integer, default=0)

    order_id = Column(Integer, ForeignKey('order.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'), primary_key=True)

    order = relationship('Order', back_populates='order_entries', uselist=False)
    product = relationship('Product', back_populates='order_entries', uselist=False)


class Product:
    __tablename__ = 'product'
    ...

    order_entries = relationship('OrderEntry', back_populates='product')


Base.metadata.create_all(engine)




from models import Base
target_metadata = Base.metadata







engine = create_engine(f'sqlite:////{DB_PATH}', echo=True)
if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)

Session = sessionmaker(engine)
session = Session()

u = User(username='admin', password='admin')
session.add(u)
session.commit()






session.query(User).filter_by(username='admin')
session.query(User).filter_by(username='admin').first()
session.query(User).filter_by(username='admin').one()

session.query(User).filter_by(username='admin').update({'password': 'new_password'})
session.query(User).filter_by(username='admin').first().update({'password': 'new_password'})

session.query(User).filter(User.username == 'admin')
session.query(User).filter(User.age >= 18)

user = session.query(User).filter(User.username == 'admin')
user.password = 'new_password'
session.add(user)
session.commit()

user = User(username='new_user', password='pass')
session.add(user)
session.commit()
