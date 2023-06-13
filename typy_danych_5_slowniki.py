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
