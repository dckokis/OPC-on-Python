# ax^2+bx+c=0
a = int(input("input a:"))
b = int(input("input b:"))
c = int(input("input c:"))
if a == 0:
    if b == 0:
        if c == 0:
            print("infinite amount of answers")
        else:
            print("no answer")
    else:
        x = -c / b
        print(x)
else:
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = ((-b + d ** (1 / 2)) / (2 * a))
        x2 = ((-b - d ** (1 / 2)) / (2 * a))
        print(x1, x2)
    elif d == 0:
        x1 = ((-b + d ** (1 / 2)) / (2 * a))
        print(x1)
    elif d < 0:
        print("no answer")

