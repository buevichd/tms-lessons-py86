VOWELS = ['a', 'e', 'i', 'o', 'u']


def remove_vowels(chars: list[str]) -> list[str]:
    return list(filter(lambda x: x not in VOWELS, chars))


chars = input().split()
print(remove_vowels(chars))

