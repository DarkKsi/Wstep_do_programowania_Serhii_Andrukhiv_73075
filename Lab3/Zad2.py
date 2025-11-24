import string

zdanie = input("Podaj zdanie: ")

#A)

litery_w_zdaniu = zdanie.lower().replace(" ", "")
litery_w_zdaniu = list(set(litery_w_zdaniu))
litery_w_zdaniu = sorted(litery_w_zdaniu)

alphabet = string.ascii_lowercase
brakujance = list()

for i in alphabet:
    if i not in litery_w_zdaniu:
        brakujance.append(i)

print("Litery obecne: ",litery_w_zdaniu)
print("Litery brakujące: ", brakujance)

#B)
parzyste_indeksy = zdanie[::2]
print("Bez znaków o nieparzystych indeksach:", parzyste_indeksy)

#C)

wyrazy = zdanie.split()
nowe_wyrazy = list()

for w in wyrazy:
    if len(w) == 1:
        nowe_wyrazy.append(w.upper())
    else:
        nowe = w[0].upper() + w[1:-1] + w[-1].upper()
        nowe_wyrazy.append(nowe)

print("Wyrazy z wielkimi pierwszą i ostatnią literą: ", " ".join(nowe_wyrazy))

#D)

najdluzsze = max(wyrazy, key=len)
print("Najdłuższe słowo:", najdluzsze)
print("Długość:", len(najdluzsze))

#E)

widzialem = set()
wynik = ""

for ch in zdanie:
    if ch in widzialem:
        wynik += "@"
    else:
        wynik += ch
        widzialem.add(ch)

print("Po zamianie powtarzających się znaków na '@': ", wynik)