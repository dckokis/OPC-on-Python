import operator
from random import randint
import time

# Функция для разбиения массива на подмассивы
def merge_sort(array, compare=operator.lt):
    if len(array) < 2:
        return array
    else:
        mid = len(array) // 2
        left = merge_sort(array[:mid], compare)
        right = merge_sort(array[mid:], compare)
        return merge(left, right, compare)

# Функция сортировки разделенных массивов
def merge(left, right, compare):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res


arr = []
x = randint(1, 50000)
for i in range(10000):
    arr.append(randint(-x, x))
start = time.perf_counter()
merge_sort(arr)
end = time.perf_counter()
end - start
a = merge_sort(arr)


corr = True
for i in range(len(a)):
    if a[i-1] > a[i]:
        corr = False
    else:
        corr = True
assert merge_sort([2, 4, 1, 18, 10, 7, 9, 3]) == [1, 2, 3, 4, 7, 9, 10, 18]
assert merge_sort([]) == []
assert merge_sort([222]) == [222]
assert merge_sort([1, 1, 1, 1]) == [1, 1, 1, 1]

