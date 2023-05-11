class _Node:
    """Single node of a tree. Keeps references to parent, left, right and some data."""
    pass


class Tree:
    """Tree itself. Keeps root node of a tree and a comparision function."""
    pass


def create(cmp_func):
    """Create empty tree."""
    t = Tree()
    t.cmp_func = cmp_func
    t.root = None
    return t


def clear(tree):
    """Clear tree but do not destroy tree itself."""
    if tree.root is not None:
        tree.root = None
    return


def _size(node):
    if node is None:
        return 0
    return _size(node.left) + _size(node.right) + 1


def size(tree):
    """Return number of elements."""
    return _size(tree.root)


def find(tree, data):
    """Find element with equal data and return its data if any."""
    if not tree.root:
        return None

    cur = tree.root

    while True:
        cmp = tree.cmp_func(cur.data, data)
        if cmp < 0:
            if not cur.right:
                return None
            else:
                cur = cur.right
        elif cmp > 0:
            if not cur.left:
                return None
            else:
                cur = cur.left
        else:
            return cur.data


def insert(tree, data):
    """Insert data into tree and return replaced data if any."""
    if not tree.root:
        n = _Node()
        n.data = data
        n.left = n.right = None
        tree.root = n
        return

    cur = tree.root

    while True:
        cmp = tree.cmp_func(cur.data, data)
        if cmp < 0:
            if not cur.right:
                n = _Node()
                n.data = data
                n.left = n.right = None
                cur.right = n
                return
            else:
                cur = cur.right
        elif cmp > 0:
            if not cur.left:
                n = _Node()
                n.data = data
                n.left = n.right = None
                cur.left = n
                return
            else:
                cur = cur.left
        else:
            cur.data = data
            return


def delete(tree, data):
    """Delete element with equal data and return its data if any."""
    if not tree.root:
        return None
    cur = tree.root
    cmp = tree.cmp_func(cur.data, data)
    while cur.data != data:
        if cmp < 0 and cur.right:
            parent = cur
            cur = cur.right
        elif cmp > 0 and cur.left:
            parent = cur
            cur = cur.left
        else:
            return None
    if cur.left is None and cur.right is None: #дошли до cur.data == data
        removable = cur.data
        cur is None
        return removable
    if cur.left is None:
        removable = cur.data
        if tree.cmp_func(parent.data, data) > 0:
            parent.left = cur.right
        else:
            parent.right = cur.right
        return removable
    if cur.right is None:
        removable = cur.data
        if tree.cmp_func(parent.data, data) > 0:
            parent.left = cur.left
        else:
            parent.right = cur.left
        return removable
    removable = cur
    if cur.right and cur.left: #поиск минимума по правой ветке
        cur = cur.right
        parent = cur
        while cur.left:
            parent = cur
            cur = cur.left
    min = cur.data
    #нашли минимум, вытаскиваем его наверх вместо data и удаляем то, что вытащили
    removable.data = min
    parent.left = cur.right
    return removable.data


def _foreach(node, func):
    if node is None:
        return None
    _foreach(node.left, func)
    func(node.data)
    _foreach(node.right, func)


def foreach(tree, func):
    """Call func for every element's data in tree in infix-order."""
    _foreach(tree.root, func)
