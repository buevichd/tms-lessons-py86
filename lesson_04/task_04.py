import random

n = random.randint(1, 5)
while True:
    a = int(input('Enter a number: '))
    if a == n:
        print('Well done!')
        break
    else:
        print('Try again.')
