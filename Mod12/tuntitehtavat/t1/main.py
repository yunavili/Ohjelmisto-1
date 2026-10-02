from hahmoluokat import Hahmo, Pelaajahahmo, Hirvio


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