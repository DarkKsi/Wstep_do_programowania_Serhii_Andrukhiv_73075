def srednia(lista_liczb):
    if len(lista_liczb) == 0:
        return 0
    return sum(lista_liczb) / len(lista_liczb)

dane = [5, 10, 15, 20]
wynik = srednia(dane)
print("Średnia wynosi:", wynik)

dane = list()
wynik = srednia(dane)
print("Średnia wynosi:", wynik)