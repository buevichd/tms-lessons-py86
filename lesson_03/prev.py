# 1
a = int(input())
perimeter = 4 * a
square = a ** 2
diag = a * 2 ** 0.5
t = (perimeter, square, diag)
print(t)

# 2
a = int(input())
print(a % 2 == 0)

# 3
x = float(input())
y = int(input())
print(x * 1.1 ** y)

# 4
s = input()
print(tuple(set(s)))

# 5
month_days = {'january': 31, 'february': 28, 'march': 31, 'april': 30,
              'may': 31, 'june': 30, 'july': 31, 'august': 31, 'september': 30,
              'october': 31, 'november': 30, 'december': 31}
month = input().lower()
print(month_days.get(month, "Unknown month"))

# 6
month_days = {'january': 31, 'february': 28, 'march': 31, 'april': 30,
              'may': 31, 'june': 30, 'july': 31, 'august': 31, 'september': 30,
              'october': 31, 'november': 30, 'december': 31}
month = input().lower()
day = int(input())
print(0 < day <= month_days.get(month, -1))

# 7
n = int(input())
is_prime = True
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
print(is_prime)













month_days = {'january': 31, 'february': 28, 'march': 31, 'april': 30,
              'may': 31, 'june': 30, 'july': 31, 'august': 31, 'september': 30,
              'october': 31, 'november': 30, 'december': 31}







