rachunki = {
    "styczeń": 120.50,
    "luty": 135.75,
    "marzec": 110.20,
    "kwiecień": 145.00,
    "maj": 130.30
}

#A)
wartosci = list(rachunki.values())
maks = max(wartosci)
minim = min(wartosci)
suma = sum(wartosci)
srednia = suma / len(wartosci)

print(f"Maksymalny rachunek: {maks} zł")
print(f"Minimalny rachunek: {minim} zł")
print(f"Suma rachunków: {suma} zł")
print(f"Średnia wartość rachunku: {srednia:.2f} zł")

#B)
ostatni_miesiac = list(rachunki.keys())[-1]
ostatnia_wartosc = rachunki[ostatni_miesiac]

if ostatnia_wartosc > srednia:
    print("Trzeba zacisnąć pasa")
else:
    print("Wszystko okay")