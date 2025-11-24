osoby = ["Kasia", "Adam", "Bartek", "Ewa"]

# A)
osoby.sort()
print("Posortowana lista:", osoby)

# B)
osoby.append("Zofia")
osoby.append("Marek")
ostatnia = osoby.pop()

print("Lista po dodaniu i pop():", osoby)
print("Ostatnia zdjęta osoba:", ostatnia)

# C)
osoby.insert(2, "Jan")
print("Lista po dodaniu na pozycji 3:", osoby)

# D)
osoby.reverse()
print("Odwrócona lista:", osoby)
print("Zdublowana lista: ", osoby * 2)