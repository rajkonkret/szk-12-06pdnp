# dziedziczenie
class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")


class Samochod(Pojazd):
    """
    Samochod
    """

    def __init__(self, kolor, marka):
        super().__init__(kolor)
        self.marka = marka

    def info(self):
        super().info()
        print(f"Marka: {self.marka}")


pojazd = Pojazd("czerwony")
pojazd.info()
# Kolor: Biały
# Marka: Mercedes
samochod = Samochod("Biały", "Mercedes")
samochod.info()
