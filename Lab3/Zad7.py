import random

a = random.randint(3, 7)
b = random.randint(3, 7)

X = set(random.randint(0, 10) for _ in range(a))
Y = set(random.randint(0, 10) for _ in range(b))

print("Zbiór X:", X)
print("Zbiór Y:", Y)

#A)
print("Czy X zawiera 5?", 5 in X)

#B)
print("Czy X jest podzbiorem Y?", X.issubset(Y))

#C)
print("Czy Y jest podzbiorem X?", Y.issubset(X))

#D)
suma = X.union(Y)
print("Suma zbiorów X i Y:", suma)

#E)
roznica_XY = X - Y
print("Różnica X - Y:", roznica_XY)

#F)
roznica_YX = Y - X
print("Różnica Y - X:", roznica_YX)

#G)
iloczyn = X.intersection(Y)
print("Iloczyn zbiorów X i Y:", iloczyn)

#H)
if X or Y:
    najwyzszy = max(X.union(Y))
    print("Najwyższy element w obu zbiorach:", najwyzszy)
else:
    print("Oba zbiory są puste")

#I)
if X:
    pierwszy = next(iter(X))
    X.remove(pierwszy)
    Y.add(pierwszy)
    print("Po przeniesieniu pierwszego elementu z X do Y:")
    print("X:", X)
    print("Y:", Y)

#J)
Y.update(X)
print("Po przekopiowaniu wszystkich elementów X do Y:")
print("X:", X)
print("Y:", Y)

#K)
X.clear()
Y.clear()
print("Po wyczyszczeniu zbiorów:")
print("X:", X)
print("Y:", Y)