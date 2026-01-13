#Efekt A

def liczba_zwiedzajacych(bilet_normalne, bilet_ulgowy):
    return bilet_normalne + bilet_ulgowy


def przychod_dzienny(bilet_normalne, bilety_ulgowy, cena_normalna, cena_ulgow):
    return (bilet_normalne * cena_normalna) + (bilety_ulgowy * cena_ulgow)


def procent_oblozenia(pojemnosc_parku, liczba_zwiedzajacych):
    if pojemnosc_parku == 0: #Zczytujemy czy ilość zwiedzajacych nie jest 0
        return 0
    return (liczba_zwiedzajacych / pojemnosc_parku) * 100

#Efekt B

def najbardziej_dochodowy_dzien(zwiedzajacy, ceny_biletow):
    # Analizuje najbardziej dochodowy dzień tygodnia
    # Zwraca nazwę dnia oraz wartość przychodu

    dni_tygodnia = [
        "poniedziałek", "wtorek", "środa",
        "czwartek", "piątek", "sobota", "niedziela"
    ]

    przychody = []

    for i in range(len(zwiedzajacy)): #oblicza przychód dla każdego dnia tygodnia
        przychod_dnia = zwiedzajacy[i] * ceny_biletow[i]
        przychody.append(przychod_dnia)

    max_przychod = max(przychody)
    index_dnia = przychody.index(max_przychod)

    return dni_tygodnia[index_dnia], max_przychod
