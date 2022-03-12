def quicksort(a, begin=0, end=None):
    median = begin
    begin += 1
    if end is None:
        end = len(a) - 1
    while begin <= end:
        while a[begin] < a[median]:
            begin += 1
        while a[end] > a[median]:
            end -= 1
        a[begin], a[end] = a[end], a[begin]
    a[median], a[end] = a[end], a[median]
    quicksort(a, begin, median - 1)
    quicksort(a, median + 1, end)


# import random
#
# arr = [0] * 10
# for i in range(len(arr)):
#     arr[i] = random.randint(-1000, 1000)
# print(quicksort(arr, 0, None))

assert quicksort([1, 3, 2, 10, 12, 5, 6, 8, 1, 4, 11], 0, None) == [1, 1, 2, 3, 4, 5, 6, 8, 10, 11, 12]
