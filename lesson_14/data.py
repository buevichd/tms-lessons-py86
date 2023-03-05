import re


users = []
with open('data.txt') as file:
    for line in file:
        match = re.match(r'\d{0,3}\s?([\w-]+)\s([\w ]+).*?(жен|муж).*?(\d+) (года|лет).*\s([\w-]+?)\n', line)
        if match:
            users.append(f"('{match.group(1)}', '{match.group(2)}', {match.group(4)}, '{match.group(6)}')")

# sort by first name
users.sort()

print(',\n'.join(users))
