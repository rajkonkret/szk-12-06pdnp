# klasa

class Human:
    """
    Klasa opisująca człowieka w Pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    def podaj_wiek(self):
        print("Mam", self.wiek, "lat(a)")


print(Human.__doc__)
cz1 = Human()
print(cz1)  # <__main__.Human object at 0x1049db5d0>
print(type(cz1))  # <class '__main__.Human'>
print(cz1.plec)
cz1.imie = "Radek"
cz1.wiek = 48
print(cz1.wiek)
print(cz1.imie)
cz1.plec = 'm'
print(cz1.plec)
cz1.podaj_wiek()

cz2 = Human()
cz2.imie = "Robert"
cz2.plec = "m"
cz2.wiek = '34'
print(cz2.wiek)
cz2.powitanie()
cz2.podaj_wiek()  # Mam 34 lat(a)
