import random

spalanie = float(input("Podaj średnie spalanie swojego samochodu (l/100 km): "))

dystans = random.randint(25, 2490)

cena_paliwa = 6.5

zuzycie = (dystans * spalanie) / 100
koszt = zuzycie * cena_paliwa

print(f"\nWylosowana długość trasy: {dystans} km")
print(f"Przewidywane zużycie paliwa: {zuzycie:.2f} litrów")
print(f"Szacowany koszt podróży: {koszt:.2f} zł")

'''
Biblioteka random pozwala generować liczby pseudolosowe.
Są one pseudolosowe, ponieważ generowane są za pomocą algorytmu,
który wykorzystuje tzw. "ziarno" (ang. seed) do tworzenia ciągu liczb.
Gdy użyje się tego samego ziarna, można odtworzyć dokładnie taki sam ciąg,
dlatego nie są one prawdziwie losowe, a jedynie pozornie losowe.
'''