def kantor(waluta):
    print("Uruchomienie kantoru")

    def usd(kwota):
        print(f"Przeliczam dolary, ${kwota} = {kwota * 4.12} zł")

    def eur(kwota):
        print(f"Przeliczam euro, {kwota} EUR = {kwota * 4.47} zł")

    if waluta == "eur":
        return eur
    else:
        return usd


waluta = input("Podaj walute (usd/eur)")
moj_kantor = kantor(waluta)
print(type(moj_kantor))  # <class 'function'>
kwota = input("Podaj kwote")
moj_kantor(int(kwota))  # Przeliczam euro
# Przeliczam euro 4470.0
# Przeliczam euro, 1000 EUR = 4470.0 zł
# Przeliczam dolary, $5000 = 20600.0 zł
