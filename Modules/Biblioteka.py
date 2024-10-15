import datetime as dt
import os
import pickle
from .knyga import Knyga
from .skaitytojas import Skaitytojas

class Biblioteka:
    def __init__(self):
        self.knygos = self.load_knygos()
        self.skaitytojai = self.load_skaitytojai()
        if self.skaitytojai is None:
            self.skaitytojai = []

    def prideti_knyga(self, knyga):
        self.knygos.append(knyga)
        self.save_knygos()
        print(f"Knyga '{knyga.pavadinimas}' įtraukta sėkmingai!")
        
    def istrinti_knyga(self, knyga):
        if knyga in self.knygos:
            self.knygos.remove(knyga)
            self.save_knygos()
            print(f"Knyga '{knyga.pavadinimas}' pašalinta sėkmingai!")
        else:
            print(f"Knyga '{knyga.pavadinimas}' nerasta!")
            
            
    def paskolinti_knyga(self, pavadinimas, vardas, pavarde):
        skaitytojas = self.rasti_skaitytoja(vardas, pavarde)
        if skaitytojas is None:
            skaitytojas = Skaitytojas(vardas, pavarde)
            self.skaitytojai.append(skaitytojas)
            self.save_skaitytojai()
            print(f"Skaitytojas '{vardas} {pavarde}' pridėtas sėkmingai!")

        knyga = self.ieskoti_knygos(pavadinimas)
        if knyga is not None:
            if isinstance(knyga, list):
                if len(knyga) == 1:
                    knyga = knyga[0]
                else:
                    print("Rasta daugiau nei viena knyga. Prašome pasirinkti vieną knygą.")
                    return
            if knyga.pasiskolinta:
                print(f"Knyga '{knyga.pavadinimas}' jau yra paskolinta kitam skaitytojui.")
            else:
                veluojancios_knygos = [knyga for knyga in skaitytojas.pasiskolintos_knygos if knyga.grazinimo_data and knyga.grazinimo_data < dt.date.today()]
                if veluojancios_knygos:
                    print(f"Skaitytojas '{vardas} {pavarde}' turi veluojančių knygų. Prieš paskolinti naują knygą, reikia grąžinti veluojančias knygas.")
                elif len(skaitytojas.pasiskolintos_knygos) >= 5:
                    print(f"Skaitytojas '{vardas} {pavarde}' jau turi maksimalią leidžiamą knygų skaičių.")
                else:
                    knyga.pasiskolinta = True
                    knyga.grazinimo_data = dt.datetime.now() + dt.timedelta(days=10)
                    skaitytojas.pasiimti_knyga(knyga)
        else:
            print(f"Knyga '{pavadinimas}' nerasta!")

    def rasti_skaitytoja(self, vardas, pavarde):
        for skaitytojas in self.skaitytojai:
            if skaitytojas.vardas == vardas and skaitytojas.pavarde == pavarde:
                return skaitytojas
        return None