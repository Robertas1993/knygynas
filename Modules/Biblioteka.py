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