import random

szczesliwy_numerek = random.randint(1, 30)
print("Szczęśliwy numerek:", szczesliwy_numerek)

roczniki = [2003, 2004, 2002, 2001, 2005]

szczesliwy_rocznik = random.choice(roczniki)
print("Szczęśliwy rocznik:", szczesliwy_rocznik)

liczby = list(range(1, 50))
losowanie = random.sample(liczby, 6)

losowanie.sort()
print("Wynik losowania Lotto:", losowanie)