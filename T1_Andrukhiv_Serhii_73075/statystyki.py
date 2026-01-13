import park

#Efekt A
#Liczba biletów
bilety_normalne = 120
bilety_ulgowe = 80

#Ceny
cena_normalna = 50
cena_ulgowa = 30

#Maksymalna pojemność parku
pojemnosc_parku = 500

liczba_osob = park.liczba_zwiedzajacych(bilety_normalne, bilety_ulgowe)
print(f"Liczba zwiedzających: {liczba_osob}")

przychod = park.przychod_dzienny(
    bilety_normalne,
    bilety_ulgowe,
    cena_normalna,
    cena_ulgowa
)
print(f"Dzienny przychód: {przychod} zł")

oblozenie = park.procent_oblozenia(pojemnosc_parku, liczba_osob)
print(f"Procent obłożenia parku: {oblozenie:.2f}%")

# Efekt B

zwiedzajacy = [150, 180, 170, 200, 250, 400, 350]
ceny_biletow = [40, 40, 40, 45, 50, 60, 55]

dzien, przychod = park.najbardziej_dochodowy_dzien(zwiedzajacy, ceny_biletow)
print(f"Najbardziej dochodowy dzień: {dzien}, przychód: {przychod} zł")
