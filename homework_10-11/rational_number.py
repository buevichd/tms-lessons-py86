import math


class Rational:
    def __init__(self, n, d):
        self.__n = n
        self.__d = d
        self.__normalise()

    @property
    def n(self):
        return self.__n

    @property
    def d(self):
        return self.__d

    def __str__(self):
        return f'{self.n} / {self.d}'

    def __mul__(self, other: 'Rational') -> 'Rational':
        return Rational(self.n * other.n, self.d * other.d)

    def __truediv__(self, other: 'Rational') -> 'Rational':
        return self * Rational(other.d, other.n)

    def __add__(self, other: 'Rational') -> 'Rational':
        return Rational(self.n * other.d + self.d * other.n, self.d * other.d)

    def __sub__(self, other: 'Rational') -> 'Rational':
        return self + Rational(-other.n, other.d)

    def __eq__(self, other: 'Rational') -> bool:
        return self.n * other.d == other.n * self.d

    def __ne__(self, other: 'Rational') -> bool:
        return not (self == other)

    def __lt__(self, other: 'Rational') -> bool:
        return self.n / self.d < other.n / other.d

    def __le__(self, other: 'Rational') -> bool:
        return self < other or self == other

    def __gt__(self, other: 'Rational') -> bool:
        return other < self

    def __ge__(self, other: 'Rational') -> bool:
        return self > other or self == other

    def __normalise(self):
        gcd = math.gcd(self.n, self.d)
        self.__n //= gcd
        self.__d //= gcd

        if self.d < 0:
            self.__d *= -1
            self.__n *= -1


if __name__ == '__main__':
    r = Rational(1, 2)
    assert r.n == 1
    assert r.d == 2
    print(r)  # 1 / 2
    assert str(r) == '1 / 2'
    assert r * r == Rational(1, 4)
    assert r / Rational(1, 3) == Rational(3, 2)
    assert Rational(1, 2) + Rational(1, 3) == Rational(5, 6)
    assert Rational(1, 2) - Rational(1, 3) == Rational(1, 6)
    assert Rational(1, 2) > Rational(1, 3)
    assert Rational(-1, 2) <= Rational(1, 3)
    print(Rational(2, 4))
    assert str(Rational(2, 4)) == '1 / 2'
    l = Rational(1, 4) * (Rational(3, 2) + Rational(1, 8)) + Rational(156, 100)
    assert l == Rational(1573, 800)

