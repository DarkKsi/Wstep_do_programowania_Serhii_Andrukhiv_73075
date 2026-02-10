from datetime import datetime

miesiace = {
    1: "stycznia", 2: "lutego", 3: "marca", 4: "kwietnia",
    5: "maja", 6: "czerwca", 7: "lipca", 8: "sierpnia",
    9: "września", 10: "października", 11: "listopada", 12: "grudnia"
}

ostatnie_lab = datetime(2026, 1, 15)
kolokwium = datetime(2026, 2, 20)

dzis = datetime.now()

dni_od_lab = (dzis - ostatnie_lab).days
dni_do_kolokwium = (kolokwium - dzis).days

lab_data = f"{ostatnie_lab.day} {miesiace[ostatnie_lab.month]} {ostatnie_lab.year}"
kol_data = f"{kolokwium.day} {miesiace[kolokwium.month]} {kolokwium.year}"

print("Ostatnie laboratoria były:", lab_data)

if dni_od_lab >= 0:
    print("Minęło dni od laboratoriów:", dni_od_lab)
else:
    print("⚠Laboratoria jeszcze się nie odbyły!")

print("\nKolokwium będzie:", kol_data)

if dni_do_kolokwium >= 0:
    print("Zostało dni do kolokwium:", dni_do_kolokwium)
else:
    print("Kolokwium już się odbyło!")
