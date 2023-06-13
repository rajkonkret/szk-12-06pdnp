dictionary = {'imie': 'Radek', 'nazwisko': 'Kowalski'}

print(dictionary)  # {'imie': 'Radek', 'nazwisko': 'Kowalski'}
print(type(dictionary))  # <class 'dict'>

# zwraca klucze
for k in dictionary:
    print(k)

for k in dictionary.keys():
    print(k)

# wypisze warrtosci
for v in dictionary.values():
    print(v)

for k, v in dictionary.items():
    print(k, "=>", v)  # nazwisko => Kowalski

dict1 = {'name': 'imie', 'company': 'Comarch'}
print(dict1)

print({value: key for key, value in dict1.items()})
# {'name': 'imie', 'company': 'Comarch'}
# {'imie': 'name', 'Comarch': 'company'}
