import random
import string

n = int(input("Podaj liczbę elementów (n): "))
x = int(input("Podaj maksymalną długość ciągu (x): "))

lista = []
for _ in range(n):
    dl = random.randint(1, x)
    ciag = ""

    for _ in range(dl):
        ciag += random.choice(string.ascii_lowercase)
    lista.append(ciag)

krotka = tuple(lista)
print("Krotka:", krotka)

#A)

ilosc_znakow = 0

for c in krotka:
    ilosc_znakow += len(c)

print("Ilość wszystkich znaków:", ilosc_znakow)

#B)

liczba_k = 0

for c in krotka:
    liczba_k += c.count("k")
print("Liczba k:", liczba_k)

#C)

liczba_kt = 0

for c in krotka:
    if c.count("kt") > 0:
        liczba_kt += 1

print("Liczba kt:", liczba_kt)

#D)

s = int(input("Podaj wartość s: "))
dluzsze = 0

for c in krotka:
    if len(c) > s:
        dluzsze += 1

print("Ilość ciągów dłuższych niż s:", dluzsze)