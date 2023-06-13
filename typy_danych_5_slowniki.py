# słownik para klucz-wartosc {'name':"Radek"}
dict = {}  # pusty słownik
print(dict)  # {}
print(type(dict))  # <class 'dict'>

dict['imie'] = 'Radek'
print(dict)  # {'imie': 'Radek'}
dict['wiek'] = 39
print(dict)  # {'imie': 'Radek', 'wiek': 39}

print(dict.keys())
print(dict.values())
print(dict.items())  # dict_items([('imie', 'Radek'), ('wiek', 39)])

dict.update({"date": '12-12-2023'})
print(dict)  # {'imie': 'Radek', 'wiek': 39, 'date': '12-12-2023'}

dictionary = {'x': 2}
print(dictionary)
dictionary.update([('y', 3), ('z', 0)])
print(dictionary)  # {'x': 2, 'y': 3, 'z': 0}

dict2 = {'imie': 'name', 'kot': 'cat'}
print(dict2['kot'])
# dict2.update({'pies': "dog"})  # dodawanie elementu do słownika
# print("Mamy w słowniku", dict2.keys())
# key = input("Podaj słowo do przetłumaczenia")  # input zwraca str
# print(key)
# print(type(key))  # <class 'str'>
# print(dict2[key.lower().replace(" ", "")])

a = int(input("Podaj pierwsza liczbe"))
b = int(input("Podaj drugą liczbe"))
print(a + b)
