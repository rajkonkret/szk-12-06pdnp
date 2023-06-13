# for - petla iterująca
import random
from itertools import zip_longest

for i in range(10):  # 0..9
    print(i)

for i in range(10):
    pass  # nic nie rob

for _ in range(10):
    pass

for i in range(10):
    print(i * 2)

lista2 = list(range(1, 50))

for i in range(6):  # 0..5 0,1,2,3,4,5
    wyn = random.choice(lista2)
    print(wyn)
    lista2.remove(wyn)

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "jest parzysta")
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]
lista3 = []
for j in range(10):
    if j % 2 == 0:
        lista3.append(j)
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista3:
    if c == 2:
        c += 1
    print(c)  # c = c + 1

imiona = ['Radek', 'Asia', 'Zbyszek', 'Marcin']

for p in imiona:
    print(p)

# wyswietlic imiona z listy w taki sposób:
# 0 Radek
# 1 Asia
for i in range(len(imiona)):  # 0 ..3
    print(i, imiona[i])

for p, w in enumerate(imiona):
    print(p, w)

for p, w in enumerate(imiona):
    print(p, w, sep=":", end=" ")  # 0:Radek 1:Asia 2:Zbyszek 3:Marcin

ludzie = ["Radek", "Zenek", "Asia", "Marcin", "Zbyszek", "Zenek"]
wiek = [47, 67, 34, 32, 45]
jezyk = ['java', 'python']

# for p, o in enumerate(ludzie):
#     print(p, o, wiek[p])
print()
for o, w in zip(ludzie, wiek):
    print(o, w)

for o, w, j in zip(ludzie, wiek, jezyk):
    print(o, w, j)

for i, o in enumerate(zip(ludzie, wiek, jezyk)):
    print(i, o)

for i, (o, w, j) in enumerate(zip(ludzie, wiek, jezyk)):
    print(i, o, w, j)

zipped = zip_longest(ludzie, wiek, jezyk, fillvalue='Nan')
for item in zipped:
    print(item)

# ('Radek', 47, 'java')
# ('Zenek', 67, 'python')
# ('Asia', 34, 'Nan')
# ('Marcin', 32, 'Nan')
# ('Zbyszek', 45, 'Nan')
# ('Zenek', 'Nan', 'Nan')

for i in range(0, 10, 2):  # start, stop, krok
    print(i)
