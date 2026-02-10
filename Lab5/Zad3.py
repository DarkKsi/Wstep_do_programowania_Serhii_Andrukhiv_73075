import time

def sekundnik(czas):
    for i in range(czas, 0, -1):
        print("Pozostało:", i, "sekund")
        time.sleep(1)
    print("Koniec!")

t = int(input("Podaj czas w sekundach: "))
sekundnik(t)
