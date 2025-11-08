a = int(input("Podaj pierwszą liczbę całkowitą: "))
b = int(input("Podaj drugą liczbę całkowitą: "))

poczatek = min(a, b)
koniec = max(a, b)

print("Liczby parzyste w podanym przedziale:", end = "")

for i in range(poczatek, koniec + 1):
    if i % 2 != 0:
        continue
    print(i, end = " ")
