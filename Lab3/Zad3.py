tekst = input("Podaj ciąg znaków: ")

oczyszczony = tekst.replace(" ", "").lower()

if oczyszczony == oczyszczony[::-1]:
    print("To jest palindrom.")
else:
    print("To nie jest palindrom.")