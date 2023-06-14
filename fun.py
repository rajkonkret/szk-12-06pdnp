a = 4
b = 8


# deklaracja funkcji
def dodaj():
    print(a + b)


# funkcja z argumentami a i b
def dodaj2(a, b):
    print(a + b)


# funkcja z domyslną wartością argumentu
def odejmij(a, b, c=0):
    print(a - b - c)


# wywołanie funkcji
dodaj()  # 12
dodaj2(6, 7)  # 13
dodaj()
odejmij(7, 4)  # 3
odejmij(7, 4, 5)  # -2
odejmij(b=6, c=9, a=9)  # argumenty podane po nazwie
print(dodaj())  # None
# print(dodaj() + dodaj2(4, 5))
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'