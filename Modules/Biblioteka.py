Datos_vieta = r'C:\Users\Silver\knygynas\Data'
import os
import pickle


    def load_knygos(self):
        data_knygu = Datos_vieta + '\knygos.pkl'
        if os.path.exists(data_knygu):
            with open(data_knygu, 'rb') as f:
                return pickle.load(f)
        else:
            return []

    def load_skaitytojai(self):
        data_skait = Datos_vieta + '\skaitytojai.pkl'
        if os.path.exists(data_skait):
            with open(data_skait, 'rb') as f:
                return pickle.load(f)
        else:
            return None

    def save_knygos(self):
        with open(Datos_vieta + '\knygos.pkl', 'wb') as f:
            pickle.dump(self.knygos, f)

    def save_skaitytojai(self):
        with open(Datos_vieta + '\skaitytojai.pkl', 'wb') as f:
            pickle.dump(self.skaitytojai, f)