class Animal:

    def __init__(self, imie):
        self.imie = imie

    def daj_glos(self):
        pass  # nic nie rob

    def info(self):
        print(f"Imie: {self.imie}")


class Dog(Animal):
    def __init__(self, imie, rasa):
        super().__init__(imie)
        self.rasa = rasa

    def daj_glos(self):
        print("hau hau")

    def info(self):
        super().info()
        print(f"Rasa: {self.rasa}")


class Cat(Animal):
    def __init__(self, imie, kolor):
        super().__init__(imie)
        self.kolor = kolor

    def daj_glos(self):
        print("Miau Miau")

    def info(self):
        super().info()
        print(f"Kolor: {self.kolor}")


class Tiger(Cat):
    def __init__(self, imie, kolor, liczba_paskow):
        super().__init__(imie, kolor)
        self.liczba_paskow = liczba_paskow

    def daj_glos(self):
        print("Arr Arr!!!")

    def info(self):
        super().info()
        print(f"Liczba pasków: {self.liczba_paskow}")


zwierze = Animal("Bezimienny")
zwierze.info()
zwierze.daj_glos()  # niemy bo w funkcji mamy pass

pies = Dog("Burek", "Kundel")
pies.info()
pies.daj_glos()

kot = Cat("Filemon", "Szary")
kot.daj_glos()
kot.info()

tygrys = Tiger("Rajah", "Pomarańczowy", 15)
tygrys.info()
tygrys.daj_glos()
