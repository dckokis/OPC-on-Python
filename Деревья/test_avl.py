import avl_tree as avl


def cmp(x, y):
    if abs(x) < abs(y):
        return -1
    elif abs(x) > abs(y):
        return 1
    else:
        return 0


t = avl.create(cmp)

avl.insert(t, 10)
avl.insert(t, 4)
avl.insert(t, -10)
avl.insert(t, 12)
avl.insert(t, 15)
avl.insert(t, 13)
assert avl.find(t, 49) is None
assert avl.find(t, 4) == 4
assert avl.find(t, 10) == -10
assert avl.find(t, -12) == 12
assert avl.size(t) == 5

f = avl.create(cmp)
avl.insert(t, -10)
avl.insert(t, 12)
avl.insert(t, 15)
avl.insert(t, 13)

a = []
avl.foreach(t, lambda x: a.append(x**2))
print(a)


b = avl.create(cmp)
avl.insert(b, 10)
avl.insert(b, 4)
avl.insert(b, -10)
avl.insert(b, 12)
avl.insert(b, 15)
avl.insert(b, 13)
avl.clear(b)
assert avl.size(b) == 0

c = avl.create(cmp)
avl.insert(c, 4)
avl.insert(c, -10)
avl.insert(c, 12)
avl.insert(c, 15)
avl.insert(c, 1)
assert avl.size(c) == 5
assert avl.delete(c, 4) == 4
assert avl.find(c, 4) is None
assert avl.size(c) == 4
assert avl.delete(c, 12) == 12
assert avl.delete(c, 20) is None

