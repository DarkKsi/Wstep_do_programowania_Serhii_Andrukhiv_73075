wiek = int(input("Podaj swój wiek: "))
cena = 20

if wiek < 0 or wiek > 150:
    print("Błąd: Podaj realistyczny wiek (0–120).")
elif wiek < 4:
    print("Wstęp bezpłatny!")
elif wiek < 18:
    print("Cena biletu: 10 zł.")
else:
    jestStudentem = input("Czy jesteś studentem? (tak/nie): ").strip().lower()

    if  jestStudentem == "tak":
        print(f"Cena biletu: {cena * 0.75:.2f} zł")
    elif jestStudentem == "nie":
        print("Cena biletu: 20 zł.")
    else:
        print("Nie rozpoznano odpowiedzi!")