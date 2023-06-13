# while - sterowana warunkiem
licznik = 0
while True:
    licznik += 1  # licznik = licznik + 1
    print("Komunikat!!!!")
    if licznik > 10:
        break  # przerywa działąnie pętli

print(licznik)
licznik = 0
while licznik < 10:
    print("Komunikat")
    licznik += 1

lista = []
lista2 = []

while True:
    wej = input("Podaj liczbę")  # str
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista2.append(int(wej))
print(lista)
print(lista2)
