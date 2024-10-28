import csv
import matplotlib.pyplot as plt
# Kysytään käyttäjältä ennakkoon määritellyt budjettitiedot
NyVuokra = int(input("Paljonko rahaa käytät vuokraan?: "))
NyVakuutukset = int(input("Paljonko rahaa käytät vakuutuksiin?: "))
NyRuoka = int(input("Paljonko rahaa käytät ruokaan?: "))
NySähkö = int(input("Paljonko rahaa käytät sähköön?: "))
NyLiikkuminen = int(input("Paljonko rahaa käytät liikkumiseen?: "))

# Alustetaan budjetti sanakirjaan
Budjetti = {
    "vuokra": NyVuokra,
    "vakuutus": NyVakuutukset,
    "ruoka": NyRuoka,
    "sahko": NySähkö,
    "liiku": NyLiikkuminen,
}


# Lisätään käyttäjän omia budjetti kohteita
while True:
    uusi_kohde = input("Haluatko lisätä uuden kuluerän? (k/e): ")
    if uusi_kohde.lower() != "k":
        break
    kulueran_nimi = input("Anna uuden kuluerän nimi: ")
    kulueran_summa = int(input(f"Paljonko rahaa haluat budjetoida {kulueran_nimi}?: "))
    Budjetti[kulueran_nimi] = kulueran_summa

# käyttäjän muokkaa omia budjetti kohteita
while True:
    muokkaus = input("Haluatko haluatko muutta jonkin kuluerän? (k/e): ")
    if muokkaus.lower() != "k":
        break
    print(Budjetti)
    kulueran_nimi = input("Anna muutettavan kuluerän nimi: ")
    kulueran_summa = int(input(f"Paljonko rahaa haluat budjetoida {kulueran_nimi}?: "))
    Budjetti.update({kulueran_nimi:kulueran_summa})

# tulosta budjetti csv'een
data = Budjetti.copy()
with open('Budjetti.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Key', 'Value'])
    for key, value in data.items():
        writer.writerow([key, value])

# Tulosta lopullinen budjetti
print("\nLopullinen budjetti:")
for nimi, summa in Budjetti.items():
    print(f"{nimi.capitalize()}: {summa} €")

# Piirrä budjettikohteet pylväsdiagrammina
kulut = list(Budjetti.keys())
summat = list(Budjetti.values())

plt.figure(figsize=(10, 6))
plt.bar(kulut, summat, color='skyblue')
plt.title("Budjetti eri kuluerissä")
plt.xlabel("Kuluerä")
plt.ylabel("Summa (€)")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()