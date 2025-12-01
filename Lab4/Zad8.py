def potega(a, n):
    if n == 0:
        return 1

    if n < 0:
        return 1 / potega(a, -n)

    return a * potega(a, n - 1)

print(potega(2, 5))
print(potega(3, 0))
print(potega(2, -3))
print(potega(-2, 3))
