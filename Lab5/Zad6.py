import math
import keyword

print("Funkcje w module math:")
for f in dir(math):
    if callable(getattr(math, f)):
        print(f, end=", ")
print("\n")

print("Metody typu tuple:")
for f in dir(tuple):
    if callable(getattr(tuple, f)):
        print(f, end=", ")
print("\n")

print("Funkcje w module keyword:")
for f in dir(keyword):
    if callable(getattr(keyword, f)):
        print(f, end=", ")
print("\n")
