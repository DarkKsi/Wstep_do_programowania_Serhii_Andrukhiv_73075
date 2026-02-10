import random

start = int(input("Podaj początek przedziału: "))
end = int(input("Podaj koniec przedziału: "))

losowe_liczby = tuple(random.randint(start, end) for _ in range(10))
print("Wylosowana krotka:", losowe_liczby)

produkt = 1
for liczba in losowe_liczby:
    produkt *= liczba

srednia_geometryczna = produkt ** (1/10)
print("Średnia geometryczna:", srednia_geometryczna)
