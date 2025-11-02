wiek = int(input("Podaj swój wiek: "))

if wiek < 0 or wiek > 150:
    print("Podany wiek jest nieprawidłowy! Wprowadź realistyczną wartość.")
elif wiek >= 18:
    print("Jesteś pełnoletni/a. Witamy!")
else:
    print("Nie jesteś jeszcze pełnoletni/a.")

'''
Weryfikacja zakresu (0–120) pozwala uniknąć absurdalnych wartości.
'''