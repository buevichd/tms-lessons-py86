def generate_squares(count):
    for i in range(1, count + 1):
        yield i ** 2


if __name__ == '__main__':
    for i in generate_squares(10):
        print(i)

    assert [1, 4, 9, 16, 25] == [i for i in generate_squares(5)]
