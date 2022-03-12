# Функция принимает неотсортированный массив, сортирует его
# методом "Selection Sort" и возвращает отсортированный
# массив
from random import randint


def selection_sort(arr):
    if not arr:
        return []
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
            j += 1
        arr[i], arr[min] = arr[min], arr[i]
    return arr


arr = []
x = randint(1, 10000)
for i in range(10000):
    arr.append(randint(-x, x))
a = selection_sort(arr)
corr = True
for i in range(len(a)):
    if a[i-1] > a[i]:
        corr = False
    else:
        corr = True
assert selection_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
assert selection_sort([]) == []
assert selection_sort([20]) == [20]
assert selection_sort([5, 8, 9, 2, 3]) == [2, 3, 5, 8, 9]
