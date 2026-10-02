from .hahmo import Hahmo

class Hirvio(Hahmo):
    def __init__(self, nimi, repliikki):
        super().__init__(nimi)
        self.repliikki = repliikki
        

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Repliikki: {self.repliikki}")