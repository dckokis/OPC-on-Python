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
    # НЕПРАВИЛЬНО
    remove = tree.root
    if tree.cmp_func(tree.root.data, data) == 0:
        remove.data = tree.root.data
        if tree.root.left:
            tree.root = tree.root.left
        else:
            tree.root = tree.root.right
        return remove.data

    cur = tree.root
    ancestor = tree.root

    while True:
        cmp = tree.cmp_func(cur.data, data)
        if cmp < 0 and cur.right:
            ancestor = cur
            cur = cur.right
        elif cmp > 0 and cur.left:
            ancestor = cur
            cur = cur.left
        elif cmp != 0:
            return None
        else:
            break
    if cur.left is None and cur.right is None:  # reached cur.data == data
        remove = cur.data
        return remove
    if cur.left is None:
        remove = cur.data
        if tree.cmp_func(ancestor.data, data) > 0:
            ancestor.left = cur.right
        else:
            ancestor.right = cur.right
        return remove
    if cur.right is None:
        remove = cur.data
        if tree.cmp_func(ancestor.data, data) > 0:
            ancestor.left = cur.left
        else:
            ancestor.right = cur.left
        return remove
    remove = cur
    if cur.right and cur.left:  # finding max on the left branch
        cur = cur.left
        ancestor = cur
        while cur.right:
            ancestor = cur
            cur = cur.right
    min = cur.data
    remove.data = min
    ancestor.right = cur.left
    return remove.data


def _foreach(node, func):
    if node is None:
        return None
    _foreach(node.left, func)
    func(node.data)
    _foreach(node.right, func)


def foreach(tree, func):
    """Call func for every element's data in tree in infix-order."""
    _foreach(tree.root, func)
