dystans = float(input("Podaj długość trasy (w km): "))
spalanie = float(input("Podaj średnie spalanie (w litrach na 100 km): "))

cena_paliwa = 6.5

zuzycie = (dystans * spalanie) / 100
koszt = zuzycie * cena_paliwa

print(f"\nPrzewidywane zużycie paliwa: {zuzycie:.2f} litrów")
print(f"Szacowany koszt podróży: {koszt:.2f} zł")

