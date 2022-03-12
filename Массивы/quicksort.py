import random


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)


arr = []
x = random.randint(1, 10000)
for i in range(100000):
    arr.append(random.randint(-x, x))
print(quicksort(arr))
assert quicksort([1, 3, 2, 10, 12, 5, 6, 8, 1, 4, 11]), [1, 1, 2, 3, 4, 5, 6, 8, 10, 11, 12]
