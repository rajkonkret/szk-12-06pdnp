user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001  # float - typ zmiennoprzecinkowy
liczba = 134632344532  # int

print('Witaj %s masz teraz %d lat' % (user, wiek))
# print('Witaj %s masz teraz %d lat' % (wiek, user))
print("Witaj %(user)s, masz teraz %(wiek)d lat" % {'user': user, 'wiek': wiek})
print("Witaj {} masz teraz {} lat".format(user, wiek))  # Witaj Tomek masz teraz 39 lat
print("Witaj {} masz teraz {} lat".format(wiek, user))  # Witaj 39 masz teraz Tomek lat
print(f"Witaj {user} masz teraz {wiek} lat")  # f fstring

print("Używamy wersji Python %i" % 3)
print("Używamy wersji Python %f" % 3.9)
print("Używamy wersji Python %.1f" % 3.9)
print("Używamy wersji Python %.2f" % 3.9)  # Używamy wersji Python 3.90
print("Używamy wersji Python %.0f" % 3.9)
print("Używamy wersji Python %.f" % 3.9)  # Używamy wersji Python 4
print("Używamy wersji {} Pythona".format(wersja))  # Używamy wersji 3.900001 Pythona

print(f"Uzywamy wersji Pythona {wersja}")  # Uzywamy wersji Pythona 3.900001
print(f"Uzywamy wersji Pythona {wersja:.1f}")  # Uzywamy wersji Pythona 3.9
print(f"Uzywamy wersji Pythona {wersja:.0f}")  # Uzywamy wersji Pythona 4

print(f"{user:>10}")  # "      Tomek"
print(f"{user:>20}")
print(f"{user:<30}")  # "Tomek                         "

print(liczba)
print("Nasza duza liczba {:,}".format(liczba))  # Nasza duza liczba 134,632,344,532
print("Nasza duza liczba {:,}".format(liczba).replace(",", "."))
print("Nasza duza liczba {:,}".format(liczba).replace(",", " "))
# Nasza duza liczba 134 632 344 532
