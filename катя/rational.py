class Rational:
    pass


def create(numer, denom):
    res = Rational()
    res.numer = numer
    res.denom = denom
    return res


def add(a, b):
    return create(
        a.numer * b.denom + b.numer * a.denom,
        # ------------------------------------
        a.denom * b.denom
    )


def sub(a, b):
    return create(
        a.numer * b.denom - b.numer * a.denom,
        # ------------------------------------
        a.denom * b.denom)


def mul(a, b):
    return create(
        a.numer * b.numer,
        # ----------------
        a.denom * b.denom)


def div(a, b):
    if b == ZERO:
        return None
    else:
        return create(
            a.numer * b.denom,
            # ----------------
            a.denom * b.numer)


# Возведение в целочисленную степень. power может быть отрицательным!
def power(r, power):
    return create(r.numer ** power,
                  # --------------
                  r.denom ** power)


# Возвращает -1 (a < b), 0 (a == b), 1 (a > b)
def compare(a, b):
    """
    # Возвращает -1 (a < b), 0 (a == b), 1 (a > b)
    """
    a_numer = a.numer * b.denom
    b_numer = b.numer * a.denom
    if a_numer < b_numer:
        return -1
    elif a_numer > b_numer:
        return 1
    else:
        return 0


def to_int(r):
    return int(r.numer // r.denom)


def to_float(r):
    return float(r.numer / r.denom)


def to_str(r):
    return str(r.numer) + '/' + str(r.denom)


ONE = create(1, 1)
ZERO = create(0, 1)
