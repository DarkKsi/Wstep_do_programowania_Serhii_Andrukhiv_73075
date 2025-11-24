def oblicz_bmi(waga, wzrost):
    bmi = waga / ((wzrost / 100) ** 2)

    print(f"Twoje BMI wynosi: {bmi:.2f}")

    if bmi < 18.5:
        print("Niedowaga.")
    elif 18.5 <= bmi < 25:
        print("Prawidłowa masa ciała.")
    elif 25 <= bmi < 30:
        print("Nadwaga.")
    else:
        print("Otyłość.")

waga = float(input("Podaj swoją wagę (kg): "))
wzrost = float(input("Podaj swój wzrost (sm): "))

oblicz_bmi(waga, wzrost)