import rational as r

r.create(3, 2)
a = r.create(3, 2)
b = r.create(1, 2)
c = r.add(a, b)

assert r.compare(c, r.create(2, 1)) == 0
assert r.compare(r.ONE, r.add(r.ONE, r.ONE)) < 0
assert r.div(r.ONE, r.ZERO) is None
assert r.compare(r.create(17, 15), r.mul(r.create(17, 3), r.create(1, 5))) == 0
