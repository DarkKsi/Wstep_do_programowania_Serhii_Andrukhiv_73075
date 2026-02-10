import temperatura

c = 21
f = temperatura.c_to_f(c)
print(f"{c}°C to {f:.2f}°F")

f_input = 89
c_from_f = temperatura.f_to_c(f_input)
print(f"{f_input}°F to {c_from_f:.2f}°C")

c2 = 35
k = temperatura.c_to_k(c2)
print(f"{c2}°C to {k:.2f} K")
