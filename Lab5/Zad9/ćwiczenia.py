# --------------------------
# Sposób 1: import całego modułu
import f_mat

print("=== Import całego modułu f_mat ===")
print("Kwadrat 10:", f_mat.kwadrat(10))
print("Sześcian 3:", f_mat.szescian(3))
print("Dodaj 10 + 5:", f_mat.dodaj(10, 5))

# --------------------------
# Sposób 2: import wybranych funkcji
from f_mat import kwadrat, szescian, dodaj

print("\n=== Import wybranych funkcji ===")
print("Kwadrat 10:", kwadrat(10))
print("Sześcian 3:", szescian(3))
print("Dodaj 10 + 5:", dodaj(10, 5))
