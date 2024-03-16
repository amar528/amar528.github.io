from fractions import Fraction
from functools import reduce


def product(_fracs):
    t = reduce(lambda f1, f2: f1 * f2, _fracs)
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
