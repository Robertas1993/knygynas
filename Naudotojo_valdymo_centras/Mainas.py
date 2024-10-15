from Modules.Biblioteka import *
def naudotojo_funkcija():
            
    biblioteka = Biblioteka()
    while True:
        print("Bibliotekos valdymo sistema")
        print("1. Įtraukti knygą")
        print("2. Pašalinti seną knygą")
        print("3. Pasiimti knygą išsinešimui ")
        print("4. Ieškoti knygos")
        print("5. Rodyti visas knygas")
        print("6. Peržiūrėti visas vėluojančias knygas")
        print("7 Baigti darbą")
        print("8 Visi skaitytojai")
        pasirinkimas = input("Įveskite savo pasirinkimą: ")
        if pasirinkimas == "1":
            try:
                pavadinimas = input("Įveskite knygos pavadinimą: ")
                autorius = input("Įveskite knygos autorių: ")
                leidybos_metai = int(input("Įveskite leidybos metus: "))
                zanras = input(" Įveskite žanrą: ")
                knyga = Knyga(pavadinimas, autorius, leidybos_metai, zanras)
                biblioteka.prideti_knyga(knyga)
            except ValueError as e:
                    print(f"Klaida: {e}")

        elif pasirinkimas == "2":
            try:
                knyga_pavadinimas = str(input("Įveskite knygos pavadinimą kuria norite Ištrinti "))
                for knyga in biblioteka.knygos:
                    if knyga.pavadinimas == knyga_pavadinimas:
                         biblioteka.istrinti_knyga(knyga)
                         break
                else:
                        print(f"Knyga '{knyga_pavadinimas}' nerasta!")
            except Exception as e:
                        print(f"Klaida: {e}")

        elif pasirinkimas == "3":
            try:
                pavadinimas = input("Įveskite knygos pavadinimą: ")
                vardas = input("Įveskite skaitytojo vardą: ")
                pavarde = input("Įveskite skaitytojo pavardę: ")
                biblioteka.paskolinti_knyga(pavadinimas, vardas, pavarde)
            except Exception as e:
                print(f"Klaida: {e}")


naudotojo_funkcija()
