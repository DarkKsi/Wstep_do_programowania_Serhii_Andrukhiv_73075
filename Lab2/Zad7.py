#A
imie = input("Podaj imię: ")
print("Witaj", imie)

#B
wiek = input("Podaj wiek: ")
print("Twój wiek to:", wiek)

#C
imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")

inicjaly = imie[0] + nazwisko[0]
print("Twoje inicjały:", inicjaly)

#D
tekst = input("Podaj łańcuch: ")
print(tekst * 5)

#E
a = input("Podaj pierwszy łańcuch: ")
b = input("Podaj drugi łańcuch: ")

c = a + b
print("Połączony łańcuch:", c)

#F
a = input("Podaj pierwszy łańcuch: ")
b = input("Podaj drugi łańcuch: ")

polowa_a = len(a) // 2
polowa_b = len(b) // 2

c = a[:polowa_a] + b[polowa_b:]
print("Nowy łańcuch:", c)
