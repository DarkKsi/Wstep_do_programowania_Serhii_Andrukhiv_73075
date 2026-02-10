promocje = dict()

def dodaj_promocje():
    nazwa = input("Podaj nazwę promocji: ")
    opis = input("Podaj opis promocji: ")
    rabat = float(input("Podaj rabat procentowy: "))

    promocje[nazwa] = {
        "opis": opis,
        "rabat": rabat
    }
    print("Promocja została dodana!")


def wyswietl_promocje():
    if not promocje:
        print("Brak dostępnych promocji!\n")
        return

    print("Dostępne promocje:")

    for nazwa, dane in promocje.items():
        print(f"- {nazwa}: {dane['opis']} (rabat {dane['rabat']}%)")
    print()


def usun_promocje():
    nazwa = input("Podaj nazwę promocji do usunięcia: ")

    if nazwa in promocje:
        del promocje[nazwa]
        print("Promocja została usunięta!\n")
    else:
        print("Nie znaleziono takiej promocji!\n")

def oblicz_ceny_promocji(cena_oryginalna, rabat):
    print("Cena z promocją: ", cena_oryginalna - (cena_oryginalna * rabat / 100))

def menu():
    while True:
        print("----Zarządzanie promocjami----")
        print("1. Dodaj nową promocję")
        print("2. Wyświetli dostępne promocje")
        print("3. Usuń promocję")
        print("4. Oblicz ceny z promocji")
        print("5. Zakończ")
        print("------------------------------")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            dodaj_promocje()
        elif wybor == "2":
            wyswietl_promocje()
        elif wybor == "3":
            usun_promocje()
        elif wybor == "4":
            oblicz_ceny_promocji(int(input("Ceny: ")), int(input("Rabat procentowy: ")))
        elif wybor == "5":
            print("Koniec programu.\n")
            break
        else:
            print("Nieprawidłowy wybór!\n")


menu()
