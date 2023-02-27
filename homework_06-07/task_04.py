from functools import reduce


def my_join(words: list[str], sep: str) -> str:
    return reduce(lambda x, y: x + sep + y, words)


words = input().split()
sep = input()

print(my_join(words, sep))
# print(sep.join(words))
# print(words.replace(' ', sep))
