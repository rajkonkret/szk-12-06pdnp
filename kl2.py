class Human:
    """
    klasa Human opisująca człowieka w Pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    def moj_wiek(self):
        print("Mam", self.wiek, 'lat')

    def moj_wzrost(self):
        print("Nazywam się", self.imie, "Mam", self.wiek, "lat(a)")

    def ruszaj(self):
        if self.plec == "m":
            print("Ruszyłem")
        else:
            print("Ruszyłam")


cz1 = Human("Asia", "20", 190)
print(cz1.imie)
cz1.powitanie()
cz1.ruszaj()

cz2 = Human("Radek", 80, 176, "m")
print(cz2.imie)
cz2.powitanie()
cz2.moj_wiek()
cz2.moj_wzrost()
cz2.ruszaj()
