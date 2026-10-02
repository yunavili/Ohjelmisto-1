'''
1. Lue koodi läpi, suorita se, varmista että ymmärrät, miten se toimii nyt.
2. Luo luokat Hirvio ja Pelaajahahmo. Ne molemmat perivät luokan Hahmo.
3. Muokkaa koodia niin, että lisäät Pelaajahahmo-luokalle ominaisuuden tavaralista. 
Kun pelaajahahmo-olio luodaan, se saa parametrinä listan tavaroita, jotka tallennetaan olion listaan.
4. Ylikirjoita Hahmo-luokan tulosta-metodi Pelaajahahmolle niin, että se tulostaa mukaan myös tavaralistan.
5. Muokkaa niin, että vain hirviöillä on repliikki, ei kaikilla Hahmo-olioilla.
6. Ylikirjoita Hirvio-luokan tulosta-metodi niin, että se tulostaa myös repliikin.
7. Jos ehdit: Luo peliin useampi hirviö, ja laita pelaajahahmo taistelemaan myös niiden kanssa. 
Taistelu-metodia ei tarvita sekä hahmolle että hirviölle. 
Siirrä se sille luokalle, jossa se on sinusta looginen. 
Testaa, että peli toimii järkevästi.
'''

class Hahmo:
    def __init__(self, nimi):
        self.nimi = nimi
        self.hp = 100

    def tulosta_tiedot(self):
        print(f"Hahmon nimi: {self.nimi}")
        print(f"Hahmon hp: {self.hp}")

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

class Hirvio(Hahmo):
    def __init__(self, nimi, repliikki):
        super().__init__(nimi)
        self.repliikki = repliikki
        

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Repliikki: {self.repliikki}")

hirviot = [Hirvio("Merihirviö", "Lits läts, aion syödä sinut!"), Hirvio("Metsäpeikko", "Grrr! Pois minun metsästäni!")]

aloitustavarat = ["Miekka", "Terveysjuoma"]
pelaajahahmo = Pelaajahahmo(input("Anna hahmon nimi: "), aloitustavarat)

print("Peli alkaa.")
pelaajahahmo.tulosta_tiedot()
input()

for hirvio in hirviot:
    print(f"{pelaajahahmo.nimi} kohtaa kauhean hirviön. Hirviö huutaa:")
    print(hirvio.repliikki)
    hirvio.tulosta_tiedot()
    pelaajahahmo.taistelu(hirvio)
    input()
print("Peli ohi.")