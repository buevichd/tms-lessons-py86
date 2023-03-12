class WordIterable:
    def __init__(self, text: str):
        self.words = text.split()
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= len(self.words):
            raise StopIteration
        self.counter += 1
        return self.words[self.counter - 1]


if __name__ == '__main__':
    assert ['one', 'two', 'three'] == [i for i in WordIterable('one two three')]
