def p_kola(r):
    if r > 0:
        pole = 3.14 * r ** 2
    else:
        pole = 0
    print(f"Pole koła o promieniu {r} wynosi: ", pole)

def p_kola2(r, pi = 3.14):
    if r > 0:
        pole = pi * r ** 2
        print(f"Pole koła o promieniu {r} wynosi: ", pole)
    else:
        print(f"Pole o promieniu {r} nie istnieje")

a = 8

p_kola(2)
p_kola2(a, pi = 3)
