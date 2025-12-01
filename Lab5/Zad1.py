#A

import random

liczba_osob = 20
szczesliwy_numerek = random.randint(1, liczba_osob)

print("Szczęśliwy numerek:", szczesliwy_numerek)

#B

import random

roczniki = [2004, 2005, 2003, 2004, 2006, 2005, 2003]

szczesliwy_rocznik = random.choice(roczniki)

print("Roczniki w grupie:", roczniki)
print("Szczęśliwy rocznik:", szczesliwy_rocznik)

#C

import random

liczby = list(range(1, 50))

losowanie = random.sample(liczby, 6)

losowanie.sort()

print("Wylosowane liczby:", losowanie)
