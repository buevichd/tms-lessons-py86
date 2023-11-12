import math


class Rational:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator
        self.__normalise()

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __str__(self):
        return f'{self.numerator} / {self.denominator}'

    def __mul__(self, other: 'Rational') -> 'Rational':
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other: 'Rational') -> 'Rational':
        return self * Rational(other.denominator, other.numerator)

    def __add__(self, other: 'Rational') -> 'Rational':
        return Rational(self.numerator * other.denominator + self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def __sub__(self, other: 'Rational') -> 'Rational':
        return self + Rational(-other.numerator, other.denominator)

    def __eq__(self, other: 'Rational') -> bool:
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other: 'Rational') -> bool:
        return not (self == other)

    def __lt__(self, other: 'Rational') -> bool:
        return self.numerator / self.denominator < other.numerator / other.denominator

    def __le__(self, other: 'Rational') -> bool:
        return self < other or self == other

    def __gt__(self, other: 'Rational') -> bool:
        return other < self

    def __ge__(self, other: 'Rational') -> bool:
        return other <= self

    def __normalise(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.__numerator //= gcd
        self.__denominator //= gcd

        if self.denominator < 0:
            self.__denominator *= -1
            self.__numerator *= -1


if __name__ == '__main__':
    r = Rational(1, 2)
    assert r.numerator == 1
    assert r.denominator == 2
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
