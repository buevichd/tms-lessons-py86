from my_time import MyTime


class MyTimeInterval:
    def __init__(self, start_seconds, finish_seconds):
        self.start = MyTime(start_seconds)
        self.finish = MyTime(finish_seconds)

    def is_inside(self, time: MyTime) -> bool:
        return self.start <= time <= self.finish

    def intersects(self, other: 'MyTimeInterval') -> bool:
        return self.is_inside(other.start) or self.is_inside(other.finish) or \
            other.is_inside(self.start) or other.is_inside(self.finish)


if __name__ == '__main__':
    interval = MyTimeInterval(10, 20)

    assert interval.is_inside(MyTime(15))
    assert interval.is_inside(MyTime(10))
    assert interval.is_inside(MyTime(20))
    assert not interval.is_inside(MyTime(5))
    assert not interval.is_inside(MyTime(25))

    assert interval.intersects(MyTimeInterval(5, 15))
    assert interval.intersects(MyTimeInterval(5, 25))
    assert interval.intersects(MyTimeInterval(10, 25))
    assert interval.intersects(MyTimeInterval(11, 19))
    assert not interval.intersects(MyTimeInterval(0, 5))
    assert not interval.intersects(MyTimeInterval(25, 30))
