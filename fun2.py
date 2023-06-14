# funkcja zwracająca wynik

def dodaj(a, b):
    return a + b


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(5, 6))  # 11
print(dodaj(5, 6) + dodaj(4, 3))
print(oblicz_vat(1000))  # 1230.0
print(oblicz_vat(1000, 7))  # 1070.0

zm = oblicz_vat(1000)  # float
if zm == 1230:
    print('Prawidłowo')
