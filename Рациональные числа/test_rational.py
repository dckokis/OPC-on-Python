import rational as r

a = r.create(3, 2)  # 3/2
b = r.create(1, 2)  # 1/2
c = r.add(a, b)  # 2

g = r.div(r.create(1, 3), r.create(-1, 1))
assert r.to_str(g) == "-1/3"
assert r.compare(g, r.create(-1, 2)) == 1

assert r.compare(c, r.create(2, 1)) == 0
assert r.compare(r.create(2, 4), r.create(1, 2)) == 0
assert r.compare(r.create(2, 4), r.create(1, 2)) == 0
assert r.compare(r.ONE, r.add(r.ONE, r.ONE)) < 0
assert r.compare(r.ZERO, r.add(r.create(-1, 2), r.create(1, 2))) == 0
assert r.compare(r.ZERO, r.sub(r.create(1, 2), r.create(1, 2))) == 0
assert r.compare(r.create(1, 4), r.mul(r.create(1, 2), r.create(1, 2))) == 0
assert r.compare(r.ZERO, r.mul(r.create(1, 2), r.ZERO)) == 0
assert r.compare(r.create(1, 4), r.div(r.create(1, 2), r.create(2, 1))) == 0
assert r.div(r.create(1, 2), r.ZERO) is None
assert r.compare(r.create(-1, 2), r.create(1, -4)) < 0
assert r.compare(r.create(-1, 2), r.create(1, 4)) < 0
assert r.compare(r.create(1, 2), r.create(-1, 4)) > 0
assert r.compare(r.ONE, r.power(r.create(1, 2), 0)) == 0
assert r.compare(r.create(1, 4), r.power(r.create(1, 2), 2)) == 0
assert r.compare(r.create(2, 1), r.power(r.create(1, 2), -1)) == 0
assert r.to_str(r.create(3, 2)) == "3/2"
assert r.to_int(r.create(4, 3)) == 1
assert r.to_float(r.create(3, 2)) == 1.5
assert r.div(r.create(1, 2), r.create(0, 1)) is None
assert r.div(r.create(2, 4), r.create(0, 3)) is None
assert r.compare(r.create(-1, 2), r.create(1, -2)) == 0
assert r.div(r.create(0, 5), r.create(1, 2)) == r.ZERO
assert r.to_str(r.create(1, 0)) is None
assert r.power(r.create(1, 0), 2) is None
assert r.to_int(r.create(1, 0)) is None
assert r.to_float(r.create(1, 0)) is None
assert r.compare(r.create(1, 0), r.create(2, 0)) is None
assert r.compare(r.ZERO, r.create(0, 222)) == 0
assert r.div(r.create(1, 2), r.sub(r.create(1, 2), r.create(1, 2))) is None
