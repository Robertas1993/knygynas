
Datos_vieta = r'C:\Users\Silver\knygynas\Data'

import os
import pickle
from .knyga import *
from .skaitytojas import *

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
            
    def ieskoti_knygos(self, pavadinimas_arba_autorius):
        rezultatai = []
        pavadinimas_arba_autorius = pavadinimas_arba_autorius.lower()
        for knyga in self.knygos:
            if pavadinimas_arba_autorius in knyga.pavadinimas.lower() or pavadinimas_arba_autorius in knyga.autorius.lower():
                rezultatai.append(knyga)
        if len(rezultatai) == 1:
            return rezultatai[0]
        elif len(rezultatai) > 1:
            return rezultatai
        else:
            return None
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
    def grazinti_knyga(self, pavadinimas, vardas, pavarde):
        for knyga in self.knygos:
            if knyga.pavadinimas == pavadinimas:
                if knyga.pasiskolinta:
                    knyga.pasiskolinta = False
                    knyga.grazinimo_data = None
                    knyga.skaitytojas = None
                    skaitytojas = self.rasti_skaitytoja(vardas, pavarde)
                    if skaitytojas:
                        skaitytojas.pasiskolintos_knygos.remove(knyga)
                        self.save_skaitytojai()
                        print(f"Knyga '{knyga.pavadinimas}' grąžinta sėkmingai!")
                    else:
                        print(f"Skaitytojas '{vardas} {pavarde}' nerastas!")
                else:
                    print("Knyga nėra paskolinta.")
                return

        print(f"Knyga '{pavadinimas}' nerasta!")

    def rasti_skaitytoja(self, vardas, pavarde):
        for skaitytojas in self.skaitytojai:
            if skaitytojas.vardas == vardas and skaitytojas.pavarde == pavarde:
                return skaitytojas
        return None


    def load_knygos(self):
        data_knygu = Datos_vieta + '\knygos.pkl'
        try:
            if os.path.exists(data_knygu):
                with open(data_knygu, 'rb') as f:
                    return pickle.load(f)
            else:
                return []
        except FileNotFoundError:
            print("The file was not found.")
            return []
        except pickle.UnpicklingError:
            print("Error unpickling the file.")
            return []
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []

    def load_skaitytojai(self):
        data_skait = Datos_vieta + '\skaitytojai.pkl'
        try:
            if os.path.exists(data_skait):
                with open(data_skait, 'rb') as f:
                    return pickle.load(f)
            else:
                return None
        except FileNotFoundError:
            print("The file was not found.")
            return None
        except pickle.UnpicklingError:
            print("Error unpickling the file.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def save_knygos(self):
        try:
            with open(Datos_vieta + '\knygos.pkl', 'wb') as f:
                pickle.dump(self.knygos, f)
        except pickle.PicklingError:
            print("Error pickling the data.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def save_skaitytojai(self):
        try:
            with open(Datos_vieta + '\skaitytojai.pkl', 'wb') as f:
                pickle.dump(self.skaitytojai, f)
        except pickle.PicklingError:
            print("Error pickling the data.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            
    def rasti_skaitytojus_su_skolomis(self):
        skaitytojai_su_skolomis = [skaitytojas for skaitytojas in self.skaitytojai if skaitytojas.pasiskolintos_knygos]
        if skaitytojai_su_skolomis:
            print("Skaitytojai su skolomis:")
            for skaitytojas in skaitytojai_su_skolomis:
                veluojancios_knygos = [knyga for knyga in skaitytojas.pasiskolintos_knygos if knyga.grazinimo_data and knyga.grazinimo_data < dt.date.today()]
                if veluojancios_knygos:
                    print(f"{skaitytojas.vardas} {skaitytojas.pavarde}:")
                    for knyga in veluojancios_knygos:
                        print(f"  - {knyga.pavadinimas} (veluoja grąžinti nuo {knyga.grazinimo_data})")
        else:
            print("Nėra skaitytojų su skolomis.")