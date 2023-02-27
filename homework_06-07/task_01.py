def map_to_tuples(chars: list[str]) -> list[tuple]:
    return list(map(lambda x: (x.upper(), x.lower()), chars))


my_list = input().split()
print(map_to_tuples(my_list))
