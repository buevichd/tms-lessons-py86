import re


def generate_word(text: str):
    for word in re.findall(r'[a-zA-Z]+', text):
        yield word


if __name__ == '__main__':
    assert ['one', 'two', 'three'] == [i for i in generate_word('one two three')]
    assert ['one', 'two', 'three'] == [i for i in generate_word('one? two! three123...')]


