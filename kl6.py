class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja


class Menedzer(Pracownik):
    """
    klasa menadzer
    """

    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensje(self):
        return self.premia + self.pensja


pracownik = Pracownik("Jan", "Kowalski", 5000)
pracownik.przedstaw_sie()
wynagrodzenie_pracownik = pracownik.oblicz_pensje()
print(f"Wynagrodzenie dla pracownika {pracownik.imie}"
      f" {pracownik.nazwisko}: wynagrodzenie {wynagrodzenie_pracownik}")
# Cześć, jestem Jan Kowalski
# wynagrodzenie dla pracownika Jan Kowalski: wynagrodzenie 5000
menago = Menedzer("Anna", "Nowak", 8000, 2000)
menago.przedstaw_sie()
wynagrodzenie_menago = menago.oblicz_pensje()
print(f"Wynagrodzenie dla menadżera {menago.imie}"
      f" {menago.nazwisko}: wynagrodzenie {wynagrodzenie_menago}")
# Wynagrodzenie dla menadżera Anna Nowak: wynagrodzenie 10000