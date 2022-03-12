import avl_tree as avl


def cmp(a, b):
    if a[0] > b[0]:
        return 1
    elif a[0] < b[0]:
        return -1
    else:
        return 0


def map_create():
    m = avl.create(cmp)
    return m


def map_add(book, name, email):
    x = (name, email)
    avl.insert(book, x)


def map_get(book, name):
    n = (name, name)
    x = avl.find(book, n)
    if x is None:
        return x
    return x[1]

def map_delete(book, name):
    n = (name, name)
    x = avl.delete(book, n)
    return x

m = map_create()
map_add(m, "Ivan", "ivanov@gmail.com")
map_add(m, "Vladimir", "vladimir.parfinenko@gmail.com")
map_add(m, "Ivan", "ivanov@mail.ru")
assert map_get(m, "Vladimir") == "vladimir.parfinenko@gmail.com"
assert map_get(m, "Ivan") == "ivanov@mail.ru"
assert map_get(m, "Kostek") is None
print(map_delete(m, "Vladimir"))