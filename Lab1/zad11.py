import math

a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

if a == 0:
    print("To nie jest równanie kwadratowe! (a nie może być równe 0)")
else:
    delta = b**2 - 4*a*c
    print(f"Delta = {delta}")

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print(f"Równanie ma dwa pierwiastki rzeczywiste: x₁ = {x1:.2f}, x₂ = {x2:.2f}")

    elif delta == 0:
        x = -b / (2 * a)
        print(f"Równanie ma jeden pierwiastek rzeczywisty: x = {x:.2f}")

    else:
        print("Równanie nie ma pierwiastków rzeczywistych.")