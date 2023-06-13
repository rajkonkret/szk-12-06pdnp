# krotka - niemutowalna, niemodyfikowalna
# zmienna, niezmienna
tupla = ("Radek",)
print(type(tupla))

tupla2 = ("Tomek", "Asia", "Zbyszek", "Marcin")
print(tupla2)  # ('Tomek', 'Asia', 'Zbyszek', 'Marcin')
print(type(tupla2))  # <class 'tuple'>

tupla3 = (43, 55, 22.34, 11, 200)
print(tupla3)
print(type(tupla3))  # <class 'tuple'>

print(tupla2.count("Tomek"))
print(tupla2.index("Asia"))

a, b = 1, 2
print(a)
print(b)

a, b = b, a
print(a, b)

tp = 1, 2, 3
print(tp)
print(type(tp))  # <class 'tuple'>

a, *b = 1, 2, 3
print(a)  # 1
print(b)  # [2, 3]

a, *b = tp
print(b)

# rozpakowanie tupli
imie, *imie2, imie3 = tupla2
print(imie, imie2, imie3)  # Tomek ['Asia', 'Zbyszek'] Marcin

lista = list(tupla2)
print(lista)  # ['Tomek', 'Asia', 'Zbyszek', 'Marcin']
print(type(lista))  # <class 'list'>
