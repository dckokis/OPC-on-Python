def day_num(d=int(input("Введите число:")), m=int(input("Введите месяц:")), y=int(input("Введит год:"))):
    if d <= 0 or m <= 0 or y <= 0:
        return -1
    if m > 12:
        return -1
    count = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        count[1] += 1
    if d > count[m - 1]:
        return -1
    s = 0
    for i in range(0, m - 1):
        s = s + count[i]
    n = s + d
    return n


print(day_num())



