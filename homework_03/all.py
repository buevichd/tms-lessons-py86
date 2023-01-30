a = int(input())
perimeter = 4 * a
square = a ** 2
diag = a * 2 ** 0.5
t = (perimeter, square, diag)
print(t)

a = int(input())
print(a % 2 == 0)

x = float(input())
y = int(input())
print(x * 1.1 ** y)

s = tuple(set(input()))
print(s)

month_days = {'january': 31, 'february': 28, 'march': 31, 'april': 30,
              'may': 31, 'june': 30, 'july': 31, 'august': 31, 'september': 30,
              'october': 31, 'november': 30, 'december': 31}
month = input()
print(month_days.get(month.lower(), "Unknown month"))


month = input()
day = int(input())
print(1 <= day <= month_days.get(month, -1))


a = {'a': 1}
print(f'{a}')


my_list = [1, 2, 3]
for i in my_list:
    print(i)
    i += 1
print(i)


n = int(input())
is_prime = True
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        is_prime = True
        break
print(is_prime)





