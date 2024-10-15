from .knyga import Knyga, dt
from .Biblioteka import Biblioteka
class Skaitytojas:
    def __init__(self, vardas, pavarde):
        if not vardas or not pavarde:
            raise ValueError("Visi laukai privalo būti užpildyti")
        self.vardas = vardas
        self.pavarde = pavarde
        self.pasiskolintos_knygos = []


            
