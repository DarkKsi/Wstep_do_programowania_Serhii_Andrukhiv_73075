plik = input("Podaj nazwę pliku: ")

if plik.endswith(".xls") or plik.endswith(".xlsx"):
    print("To jest plik arkusza Excel.")
else:
    print("To nie jest plik arkusza Excel.")