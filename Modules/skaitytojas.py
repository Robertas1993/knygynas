from .knyga import Knyga, dt
from .Biblioteka import Biblioteka
class Skaitytojas:
    def __init__(self, vardas, pavarde):
        if not vardas or not pavarde:
            raise ValueError("Visi laukai privalo būti užpildyti")
        self.vardas = vardas
        self.pavarde = pavarde
        self.pasiskolintos_knygos = []

    def pasiimti_knyga(self, knyga):
            if len(self.pasiskolintos_knygos) < 5:
                knyga.grazinimo_data = dt.date.today() + dt.timedelta(seconds=10)  
                self.pasiskolintos_knygos.append(knyga)
                print(f"{self.vardas} {self.pavarde} pasiėmė knygą '{knyga.pavadinimas}'")
            else:
                print(f"{self.vardas} {self.pavarde} jau turi {len(self.pasiskolintos_knygos)} virs limito ir negali pasiimti daugiau  knygų!")

    def prideti_skaitytoja(self, vardas, pavarde):
        skaitytojas = Skaitytojas(vardas, pavarde)
        self.skaitytojai.append(skaitytojas)
        self.save_skaitytojai()
        print(f"Skaitytojas '{vardas} {pavarde}' pridėtas sėkmingai!")
            
