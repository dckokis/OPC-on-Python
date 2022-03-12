import linked_list as ll

# Prepend
head = None
head = ll.prepend(head, 99)
head = ll.prepend(head, 42)
head = ll.prepend(head, 37)
head = ll.prepend(head, 37)

ll.foreach(head, print)
ll.foreach(head,
           lambda x: print(x ** 2))  # лямбда фунции(компактные)

head = ll.from_list([2, 3, 4])
assert head.data == 2
assert head.next.data == 3
assert head.next.next.data == 4
assert head.next.next.next is None

# Length
assert ll.length(ll.from_list([1, 2, 3])) == 3
assert ll.length(None) == 0
assert ll.length(ll.from_list([100])) == 1

# Remove
lst = ll.from_list([10, 20, 30, 40, 50, 60])
assert ll.remove(lst, 5) == (60, lst)
lst = ll.from_list([10, 20, 30, 40, 50, 60])
assert ll.remove(lst, 3) == (40, lst)
lst = ll.from_list([10, 20, 30, 40, 50, 60])
assert ll.remove(lst, 0) == (10, lst)

# Append
tail = None
tail = ll.append(tail, 10)
tail = ll.append(tail, 20)
tail = ll.append(tail, 30)
ll.foreach(tail, print)

# get
lstg = ll.from_list([11, 21, 31, 41, 51])
assert ll.get(lstg, 4) == 51
assert ll.get(lstg, 3) == 41
assert ll.get(lstg, 0) == 11
assert ll.get(lstg, 1) == 21
assert ll.get(lstg, 2) == 31
assert ll.get(lstg, 6) is None

# get_last
lstgl = ll.from_list([111, 112, 113, 114])
assert ll.get_last(lstgl) == 114
assert ll.get_last(None) is None
assert ll.get_last(ll.from_list([666])) == 666

# find
lstf = ll.from_list([12, 22, 32, 42, 52])
assert ll.find(lstf, 12) == 0
assert ll.find(lstf, 22) == 1
assert ll.find(lstf, 32) == 2
assert ll.find(lstf, 42) == 3
assert ll.find(lstf, 52) == 4
assert ll.find(lstf, 62) == -1

# remove_first
lstrf = ll.from_list([10, 20, 30, 40])
assert ll.remove_first(lstrf, 30) == lstrf
assert ll.remove_first(lstrf, 10) == lstrf
assert ll.remove_first(lstrf, 50) == lstrf

# remove_all
lstra = ll.from_list([10, 20, 30, 40, 30, 50, 30])
assert ll.remove_all(lstra, 30) == lstra
assert ll.remove_all(lstra, 10) == lstra
assert ll.remove_all(lstra, 60) == lstra
assert ll.remove_all(lstra, 40) == lstra

# copy
l = ll.from_list([10, 20, 30])
assert ll.copy(None) is None
assert ll.copy(ll.from_list([])) == ll.from_list([])
assert ll.to_list(ll.copy(l)) == ll.to_list(l)

# concat
lstcnct1 = ll.from_list([10, 20, 30])
lstcnct2 = ll.from_list([40, 50, 60])
assert ll.to_list(ll.concat(lstcnct1, lstcnct2)) == [10, 20, 30, 40, 50, 60]
empty1 = ll.from_list([])
empty2 = ll.from_list([])
assert ll.to_list(ll.concat(empty1, empty2)) == []

# find_custom
lstfk = ll.from_list([20, 30, 40, 11, 100])
assert ll.find_custom(lstfk,
                      lambda x: (x // 100 == 0)) == (20, 0)
assert ll.find_custom(lstfk,
                      lambda x: (x % 3 == 0)) == (30, 1)
assert ll.find_custom(lstfk,
                      lambda x: (x == 0)) is None
