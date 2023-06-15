from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkościa", self.szybkosc)

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print(f"Tu {self.gatunek}, ja nie latam.")

    def wydaj_odglos(self):
        print("Kokokokokokokok")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")


class Orzel(Ptak):
    def wydaj_odglos(self):
        print("piiiiiiiiiiiii")

    def poluj(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie")


# TypeError: Can't instantiate abstract class Ptak with abstract method wydaj_odglos

# or1 = Ptak("Orzeł", 20)
# or1.latam()
# or1.wydaj_odglos()
# 
# kur1 = Ptak("Kura", 0)
# kur1.latam()
# kur1.wydaj_odglos()

kur2 = Kura("kura")
kur2.latam()  # Tu kura, ja nie latam.
kur2.wydaj_odglos()
kur2.dziobanie()

or2 = Orzel("Orzel", 20)
or2.latam()
or2.wydaj_odglos()
or2.poluj()
