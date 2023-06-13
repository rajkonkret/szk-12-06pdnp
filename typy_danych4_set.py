# set - przechowuje niezduplikowane elemnty

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
# nie pamieta kolejnosci

zb2 = set()  # pusty set
print(zb2)  # set()

zbior.add(33)
zbior.add(18)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}

print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 44, 18, 22, 55}
print(zbior.pop())  # 66
print(zbior.pop())  # 777
print(zbior.pop())  # 11

zbior.remove(55)
zbior.remove(18)
print(zbior)  # {44, 22}

lista2 = list(zbior)
print(lista2)
print(type(lista2))

zbior2 = {667, 11, 44, 18, 52, 62, 999, 999}
print(zbior2)

print(zbior | zbior2)  # suma zbiorow
print(zbior & zbior2)  # {44} - czesc wspolna
print(zbior - zbior2)  # różnica
print(zbior.difference(zbior2))  # {22}
print(zbior2.difference(zbior))  # {999, 11, 18, 52, 667, 62}
