def generate_word(text: str):
    for word in text.split():
        yield word


if __name__ == '__main__':
    assert ['one', 'two', 'three'] == [i for i in generate_word('one two three')]
