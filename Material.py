## KUTUPHANELER
from random import randint

name = "Ceviz3"
cekirdek = "Rr"
sitoplazma = "F"

# print(f"Name: {name} - Cekirdek: {cekirdek} - Sitoplazma: {sitoplazma}")

name2 = "Ceviz2"
cekirdek2 = "rr"
sitoplazma2 = "F"


# print(f"Name: {name2} - Cekirdek: {cekirdek2} - Sitoplazma: {sitoplazma2}")

name3 = "Ceviz1"
cekirdek3 = "RR"
sitoplazma3 = "S"

# print(f"Name: {name} - Cekirdek: {cekirdek} - Sitoplazma: {sitoplazma}")

material = []

# For loop kullanarak 1-100'e kadar olan sayilari dondur
for x in range(1,101):
    # PSEUDO CODE
    rastgeleCekirdek = ""
    # 0-100 arasinda rastgele bir sayi getir
    rastgeleSayi = randint(0,100)
        # bu sayi 0-33 arasindaysa RR
    if(rastgeleSayi < 33):
        rastgeleCekirdek = "RR"
        # bu sayi 33-66 arasindaysa Rr
    elif(rastgeleSayi < 66):
        rastgeleCekirdek = "Rr"
        # bu sayi 66-100 arasindaysa rr
    elif(rastgeleSayi < 100):
        rastgeleCekirdek = "rr"

    material.append(f"Gul{x} - Cekirdek:{rastgeleCekirdek}")

class Materyal:

    def __init__(self,isim,cekirdek,sitoplazma):
        self.isim = isim
        self.cekirdek = cekirdek
        self.sitoplazma = sitoplazma

    def detaylar(self):
        print(f"Materyal: {self.isim} - Cekirdek: {self.cekirdek} - Sitoplazma: {self.sitoplazma}")

material1 = Materyal("Kestane1","RR","F")
material2 = Materyal("Kestane2","Rr","S")
material3 = Materyal("Emin","Kartci","1999")

material1.detaylar()
material2.detaylar()
material3.detaylar()


