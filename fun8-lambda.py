# lambda - skrocony zapis funkcji
odejmij = lambda a, b: a - b  # lambda zwraca wynik(return)
print(odejmij(8, 6))

# def odejmij(a, b):
#     return a - b

oblicz_vat = lambda cena, vat=7: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 23))  # 1230.0

wiek = lambda x: "dziecko" if x < 10 else \
    ("nastolatek" if x < 18 else "dorosły")

print(wiek(9))
print(wiek(10))
print(wiek(50))

lista = [1, 2, 3, 8, 10, 23, 50]
# map() - bierze kolekcje i wykonuje naniej jkas czynnosc
print(f"Zastosowanie map: {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map: [2, 4, 6, 16, 20, 46, 100]

# filter() - filtruje kolekcje wg warunku - zwraca elemnty spełniajace warunek
print(f"Zastosowanie filter: {list(filter(lambda x: x < 3, lista))}")
# Zastosowanie filter: [1, 2]
print(f"Zastosowanie filter: {list(filter(lambda x: x > 8, lista))}")
# Zastosowanie filter: [10, 23, 50]
# wyfiltrowac wieksze od 3 a mniejsze od 20
print(f"Zastosowanie filter: {list(filter(lambda x: 3 < x < 20, lista))}")
# x > 3 and x < 20 = 3 < x < 20
