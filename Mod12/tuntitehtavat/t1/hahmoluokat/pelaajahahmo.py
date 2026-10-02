from .hahmo import Hahmo

class Pelaajahahmo(Hahmo):
    def __init__(self, nimi, tavaralista):
        super().__init__(nimi)
        self.tavaroita = list(tavaralista)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Hahmon tavaroita: {self.tavaroita}")

    def taistelu(self, vastustaja):
        print("Tulee suuri taistelu.")
        input()
        if vastustaja.hp > self.hp:
            print(f"{self.nimi} hävisi taistelun :<")
            self.hp = 0
        else:
            print(f"{self.nimi} voitti taistelun!")
            self.tulosta_tiedot()