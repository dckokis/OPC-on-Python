class Rational:
    pass


def create(numer, denom):
    if denom == 0:
        return None
    r = Rational()
    r.numer = numer
    r.denom = denom
    if denom < 0:
        r.numer = numer * (-1)
        r.denom = denom * (-1)
    for i in range(2, abs(r.numer)):
        while (r.numer % i == 0) and (r.denom % i == 0):
            r.numer = r.numer // i
            r.denom = r.denom // i
    return r


# constants
ONE = create(1, 1)
ZERO = create(0, 1)


def add(a, b):  # сложение
    return create(
        a.numer * b.denom + b.numer * a.denom,
        a.denom * b.denom
    )


def sub(a, b):  # вычитание
    return create(
        a.numer * b.denom - b.numer * a.denom,
        a.denom * b.denom
    )


def mul(a, b):  # умножение
    return create(
        a.numer * b.numer, a.denom * b.denom
    )


def div(a, b):  # деление
    """
    Выполняет деление рациональных чисел, при условии, что делитель ненулевой
    """
    if compare(b, ZERO) == 0:
        return None
    if a.numer == 0:
        return ZERO
    return create(
        a.numer * b.denom, a.denom * b.numer
    )


# Возведение в целочисленную степень. power может быть отрицательным!
def power(r, power):
    """
    Возводит число в целочисленную степень
    Показатель степени может быть как >=0, так и <0
    """
    if r is None:
        return None
    if power < 0:
        return create(
            r.denom ** (power * (-1)), r.numer ** (power * (-1))
        )
    return create(
        r.numer ** power, r.denom ** power
    )


def compare(a, b):
    """
    Возвращает -1 (a < b), 0 (a == b), 1 (a > b)
    """
    if a is None or b is None:
        return None
    a_num = a.numer * b.denom
    b_num = b.numer * a.denom
    if a_num < b_num:
        return -1
    elif a_num > b_num:
        return 1
    else:
        return 0


def to_int(r):  # перевод в целые
    if r is None:
        return None
    return r.numer // r.denom


def to_float(r):  # перевод в float
    if r is None:
        return None
    return r.numer / r.denom


def to_str(r):  # перевод в строку
    if r is None:
        return None
    if r.numer % r.denom == 0:
        return str(r.numer // r.denom)
    return str(r.numer) + "/" + str(r.denom)