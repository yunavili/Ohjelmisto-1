import os

if os.path.exists("save.txt"):
    os.remove("save.txt")
else:
    print("Tiedostoa ei loydy")