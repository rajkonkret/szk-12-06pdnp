class Car:
    """
    klasa samochód
    """

    def __init__(self, model, year=2000):
        self.model = model
        self.year = year
        # oznaczylismy jako prywatne
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10
        self.__zmien_bieg()

    def licznik(self):
        print("Prędkość wynosi", self.__predkosc, "km/h")

    def hamuj(self):
        """
        klasa hamuj
        :return: metoda zmniejsza o 10 predkosc za każdym wywołaniem
        """
        self.__predkosc -= 10

    def __zmien_bieg(self):
        print("Zmiana biegu")


car1 = Car("Ford", 2020)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# print(car1.__predkosc)  # 50
car1.licznik()  # Prędkość wynosi 50 km/h
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()
# print(car1.__predkosc)
