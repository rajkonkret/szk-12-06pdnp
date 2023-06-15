class Dom:
    """
    To jest kalsa Dom
    """

    def __init__(self, metraz, kolor, liczba_okien):
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def podaj_kolor(self):
        print(f"Mamy {self.__kolor} kolor")

    def podaj_metraz(self):
        print(f"Mamy metraż {self.__metraz}")

    def podaj_okna(self):
        print(f"Mamy {self.__liczba_okien} okna(ien)")

    def zmien_metraz(self):
        wybor = int(input("Podaj nowy metraż"))
        self.__metraz = wybor
        print("Metraż wynosi:", self.__metraz)

    def zmien_kolor(self):
        wybor = input("Podaj nowy kolor")
        self.__kolor = wybor
        print("Zmieniony kolor:", self.__kolor)

    def zmien_okna(self):
        wybor = int(input("Podaj liczbę okien"))
        self.__liczba_okien = wybor
        print("Mamy:", self.__liczba_okien, "okna(ien)")


# dom1 = Dom("500", "szary", 15)
# # print(dom1.__metraz)
# dom1.__metraz = 200  # warning
# dom1.podaj_kolor()
# dom1.podaj_okna()
# dom1.podaj_metraz()
# dom1.zmien_metraz()
# dom1.podaj_metraz()

dom2 = Dom(70, "biały", 7)
dom2.podaj_kolor()
dom2.zmien_metraz()