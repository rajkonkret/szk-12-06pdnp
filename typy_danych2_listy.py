# lista - kolekcja do przechowywania danych
lista = []  # pusta lista
print(type(lista))  # <class 'list'>
print(lista)  # []
lista.append("Radek")
lista.append("MAciek")
lista.append("Marcin")
lista.append("Asia")
lista.append("Zbyszek")
print(lista)
# ['Radek', 'MAciek', 'Marcin', 'Asia', 'Zbyszek']
# numpy
# indeksy od 0, wyswietlenie elemntu po indeksiw lista[0]
print(lista[0])
print(lista[1])
# print(lista[10])  # IndexError: list index out of range
print(lista[-1])
print(lista[-2])

print(len((lista)))  # podaje długosc listy, ta lista długosc 5
print(lista)
# ['Radek', 'MAciek', 'Marcin', 'Asia', 'Zbyszek']
lista[2] = "Mikołaj"
print(lista)  # ['Radek', 'MAciek', 'Mikołaj', 'Asia', 'Zbyszek']

lista.insert(1, "Marcin")
print(lista)
# ['Radek', 'Marcin', 'MAciek', 'Mikołaj', 'Asia', 'Zbyszek']

# usunięcie elementu z listy
lista.remove("MAciek")
print(lista)  # ['Radek', 'Marcin', 'Mikołaj', 'Asia', 'Zbyszek']

indeks = lista.index("Asia")
print(indeks)  # ['Radek', 'Marcin', 'Mikołaj', 'Asia', 'Zbyszek']

lc2 = lista
print(lc2)

lista_copy = lista.copy()
print(lista_copy)
a = 3
b = a
print(b)

lista.clear()
print(lista)
print(lista_copy)
print(lc2)

print("Radek" in lista_copy)  # True

liczby = [54, 999, 34, 22, 12.34, 687]
print(liczby)
liczby.sort()
print(liczby)  # [12.34, 22, 34, 54, 687, 999]

lista2 = ['radek', 'ola']
lista2.sort()
print(lista2)

liczby.reverse()
print(liczby)

liczby[3] = 6666
print(liczby)  # [999, 687, 54, 6666, 22, 12.34]

print(liczby[0:3])  # [999, 687, 54]
print(liczby[-2])
print(liczby[0:-2])  # [999, 687, 54, 6666]
print(liczby[2:])  # [54, 6666, 22, 12.34]

liczby.remove(54)
print(liczby)  # [999, 687, 6666, 22, 12.34]

indeks = liczby.index(6666)
print(liczby.pop(indeks))  # 6666
print(liczby)  # [999, 687, 22, 12.34]

print(len(liczby))  # 4

krotka = tuple(liczby)
print(krotka)  # (999, 687, 22, 12.34)
print(type(krotka))  # <class 'tuple'>
