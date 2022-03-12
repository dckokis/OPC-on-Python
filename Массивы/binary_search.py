# Функция принимает отсортированный массив и элемент, и выводит индекс элемента в массиве
def binary_search(arr, key):
    if not arr:
        return None
    n = len(arr)
    mid = n // 2
    low_index = 0
    high_index = n - 1
    while key != arr[mid] and low_index <= high_index:
        if key < arr[mid]:
            high_index = mid - 1
        else:
            low_index = mid + 1
        mid = (high_index + low_index) // 2
    if low_index > high_index:
        return None
    if key == arr[mid]:
        leftmost_pos = -1
        for i in range(1, mid + 1):
            if arr[mid - i] == arr[mid]:
                leftmost_pos = mid - i
        if leftmost_pos != -1:
            return leftmost_pos
    return mid


print(binary_search([1, 3, 5, 7, 8, 9, 99, 100, 102, 106, 101], 8))
assert 1 == binary_search([5, 10, 20], 10)
assert binary_search([], 8) is None
assert 0 == binary_search([9], 9)
assert binary_search([6, 8, 9], 11) is None
assert binary_search([6, 8, 9], 3) is None
assert 2 == binary_search([1, 10, 20, 30], 20)
assert 4 == binary_search([1, 3, 5, 8, 12], 12)
assert 1 == binary_search([1, 3, 3, 3, 12], 3)
assert 1 == binary_search([1, 3, 3, 3, 12, 15], 3)
assert 3 == binary_search([1, 4, 7, 10], 10)
assert 0 == binary_search([2, 4, 7, 18], 2)
assert 4 == binary_search([1, 4, 5, 10, 20], 20)
assert binary_search([6, 8, 9, 13], 11) is None
assert 0 == binary_search([3, 3, 3, 3, 3, 3], 3)
