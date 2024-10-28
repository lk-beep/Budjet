Budjet = int(input("Paljonko rahaa sinulla on budjetoida? "))
Vuokra = int(input("Paljonko rahaa käytät vuokraan? "))
Vakuutukset = int(input("Paljonko rahaa käytät Vakuutuksiin? "))
Ruoka = int(input("Paljonko rahaa käytät ruokaan? "))
Sähkö = int(input("Paljonko rahaa käytät sähköön? "))
Liikkuminen = int(input("Paljonko rahaa käytät Liikkumiseen? "))

Budjetti = {
    "maksimi": Budjet,
    "vuokra": Vuokra,
    "vakuutus": Vakuutukset,
    "ruoka": Ruoka,
    "sähkö": Sähkö,
    "liiku": Liikkuminen,
}
if Budjet > Vuokra + Vakuutukset + Ruoka + Sähkö + Liikkuminen:
    print("Budjettia ei tarvitse muuttaa")
elif Budjet < Vuokra + Vakuutukset + Ruoka + Sähkö + Liikkuminen:
    print("Budjetti pitää muuttaa")
    
print(Budjetti)