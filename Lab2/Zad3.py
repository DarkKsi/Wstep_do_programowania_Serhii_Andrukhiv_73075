n = int(input("Podaj liczbę elementów ciągu (n): "))
a = float(input("Podaj pierwszy wyraz ciągu (a): "))
r = float(input("Podaj różnicę ciągu (r): "))

print("Ciąg arytmetyczny: ", end="")
for i in range(n):
    wyraz = a + i * r
    print(wyraz, end=" ")