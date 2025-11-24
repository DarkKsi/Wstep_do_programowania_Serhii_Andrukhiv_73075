zakupy = {
    "chleb": 5.50,
    "mleko": 3.20,
    "jajka": 7.00,
    "masło": 6.50,
    "jogurt": 4.00,
    "woda": 2.50,
    "cola": 6
}

print("Lista zakupów:")
for artykul, kwota in zakupy.items():
    print(f"{artykul}: {kwota} zł")

suma = sum(zakupy.values())
print(f"\nŁączne wydatki: {suma} zł")