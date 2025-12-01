import math

def pole_trojkata(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)

    if (a <= 0 or b <= 0 or c <= 0):
        print("Boki muszą być dodatnie.")
        return

    if (a + b <= c or a + c <= b or b + c <= a):
        print("Z podanych boków nie da się zbudować trójkąta.")
        return

    s = (a + b + c) / 2
    pole = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return pole

print(pole_trojkata(3, 4, 5))
print(pole_trojkata(1, 2, 10))
