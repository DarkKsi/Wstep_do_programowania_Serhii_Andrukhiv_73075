list = list()
list.append(float(input("Podaj pierwszą liczbę (x): ")))
list.append(float(input("Podaj drugą liczbę (y): ")))
list.append(float(input("Podaj trzecią liczbę (z): ")))

for i in range(len(list) - 1):
    for j in range(len(list) - 1 - i):
        if list[j] > list[j + 1]:
            value = list[j]
            list[j] = list[j + 1]
            list[j + 1] = value

print("Liczby w kolejności rosnącej:", list)