VOWELS = ['a', 'e', 'i', 'o', 'u']


def remove_vowels(chars: list[str]) -> list[str]:
    return list(filter(lambda x: x.lower() not in VOWELS, chars))


chars = input().split()
print(remove_vowels(chars))

