with open("ostoslista.txt", "r") as file:
     sisalto = file.read()
     print(sisalto)

with open("ostoslista.txt", "r") as file:
     rivit = file.readlines()
     print(f"Tuotteita listalla: {len(rivit)}")

