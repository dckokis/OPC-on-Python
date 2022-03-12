class LinkedList:
    pass


def length(lst):
    """ Подсчитать длину списка. """
    count = 0
    cur = lst
    while cur is not None:
        cur = cur.next
        count += 1
    return count


def prepend(lst, data):  # добавить спереди
    """ Добавить в голову. Возвращает новое начало списка. """
    elem = LinkedList()
    elem.data = data
    elem.next = lst
    return elem


def get(lst, index):
    """ Возвращает данные элемента по его порядковому номеру. """
    if index > length(lst):
        return None
    cur = lst
    i = 0
    while i != index:
        cur = cur.next
        i += 1
    return cur.data


def remove(lst, index):
    """ Удаляет элемент по его порядковому номеру. Возвращает его данные и новое начало списка. """
    if index >= length(lst):
        return None
    cur = lst
    if index == 0:
        return lst.data, lst
    i = 0
    while i != index - 1:
        cur = cur.next
        i += 1
    data = cur.next.data
    cur.next = cur.next.next
    return data, lst


def append(lst, data):
    """ Добавить в хвост. Возвращает новое начало списка. """
    if not lst:
        return prepend(lst, data)
    cur = lst
    while cur.next:
        cur = cur.next
    cur.next = LinkedList()
    cur.next.data = data
    cur.next.next = None
    return lst


def get_last(lst):
    """ Возвращает данные последнего элемента. """
    if lst is None:
        return None
    cur = lst
    while cur.next:
        cur = cur.next
    return cur.data


def find(lst, data):
    """ Возвращает индекс первого элемента, равного данному. Если такого элемента нет, то возвращает -1. """
    cur = lst
    index = 0
    while cur.data != data and cur.next:
        cur = cur.next
        index += 1
    if cur.data != data and cur.next is None:
        return -1
    return index


def remove_first(lst, data):
    """ Удалить первый элемент из списка со значением data. Возвращает новое начало списка. """
    cur = lst
    while cur.next and cur.next.data != data:
        cur = cur.next
    if not cur.next:
        return lst
    cur.next = cur.next.next
    return lst


def remove_all(lst, data):
    """ Удалить все элементы из списка со значением data. Возвращает новое начало списка. """
    cur = lst
    while cur.next:
        if cur.next.next and cur.next.data == data:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return lst


def copy(lst):
    """ Скопировать список. Возвращает начало копии. """
    lst_copy = None
    cur = lst
    while cur:
        lst_copy = append(lst_copy, cur.data)
        cur = cur.next
    return lst_copy


def concat(lst1, lst2):
    """ Присоединяет в хвост списка lst1 список lst2. Возвращает новое начало объединенного списка. """
    cur = lst2
    while cur:
        append(lst1, cur.data)
        cur = cur.next
    return lst1


def find_custom(lst, predicate):
    """ Возвращает значение и индекс первого элемента, для которого данная функция-предикат возвращает истину. """
    cur = lst
    index = 0
    while predicate(cur.data) is False and cur.next:
        cur = cur.next
        index += 1
    if predicate(cur.data) is False:
        return None
    return cur.data, index


def from_list(list):  # из питоновских списков в связные
    """ Переводит список Python  в связный список."""
    head = None
    for i in range(len(list) - 1, -1, -1):
        head = prepend(head, list[i])
    return head


def to_list(lst):
    """ Переводит связный список в список Python"""
    output = []
    foreach(lst, lambda x: output.append(x))
    return output


def foreach(lst, func):
    """ Обход списка. Функции func на каждом шаге передаются данные очередного элемента списка. """
    cur = lst
    while cur:
        func(cur.data)
        cur = cur.next
