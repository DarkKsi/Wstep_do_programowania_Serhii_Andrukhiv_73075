liczbaWierszy = int(input("Liczba wierszy: "))

print("----------------------------------------------")

for i in range(liczbaWierszy):
    for j in range(liczbaWierszy):
        print("*", end="")
    print("")

print("----------------------------------------------")

for i in range(liczbaWierszy):
    for j in range(i + 1):
        print("*", end="")
    print("")

print("----------------------------------------------")

for i in range(liczbaWierszy):
    for j in range(1, liczbaWierszy - i):
        print(" ", end="")
    for j in range(i + 1):
        print("* ", end="")
    print("")