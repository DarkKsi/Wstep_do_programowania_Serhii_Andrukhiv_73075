a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

print("Wybierz działanie:")
print("1. Dodawanie (+)")
print("2. Odejmowanie (-)")
print("3. Mnożenie (*)")
print("4. Dzielenie (/)")

dzialanie = input("Wpisz symbol działania (+, -, *, /): ")

if dzialanie == "+":
    wynik = a + b
    print(f"Wynik: {a} + {b} = {wynik}")

elif dzialanie == "-":
    wynik = a - b
    print(f"Wynik: {a} - {b} = {wynik}")

elif dzialanie == "*":
    wynik = a * b
    print(f"Wynik: {a} * {b} = {wynik}")

elif dzialanie == "/":
    if b != 0:
        wynik = a / b
        print(f"Wynik: {a} / {b} = {wynik}")
    else:
        print("Nie można dzielić przez zero!")

else:
    print("Niepoprawny wybór działania!")