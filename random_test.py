import random

# pip install random
#  pip list

# random - generowanie liczb pseudolosowe

print(random.randint(1, 6))  # int 1..6
print(random.random())  # float 0..0.9999999
print(random.random() * 6)  # float od 0 do 5.999999
print(random.randrange(6))  # int od 0..5
print(random.randrange(1, 6))  # 1..5

lista = [5, 7, 45, 34, 56]
print(random.choice(lista))

lista2 = list(range(1, 50))
print(lista2)

wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)

print(random.choices(lista2, k=6))
# [32, 48, 25, 22, 37, 17]
