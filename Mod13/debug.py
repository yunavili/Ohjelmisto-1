import os

try:
    os.remove("cat.txt")
except FileNotFoundError:
    print("Tiedostoa ei löydy ://")