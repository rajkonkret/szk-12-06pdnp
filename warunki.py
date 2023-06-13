odp = True
print(odp)
print(type(odp))  # <class 'bool'>
odp = False
if odp:
    print("Brawo")
else:
    print("Musisz się uczyć")

print("Program działa nadal")

# podatek = 0.0
#
# zarobki = int(input('Podaj dochod'))
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.6
#
# print(f"Zapłacisz {zarobki * podatek} zł")

suma_zam = 50
if suma_zam > 100:
    rabacik = 25
else:
    rabacik = 0
print(f"Rabacik wynosi {rabacik}")

rabat = 25 if suma_zam > 100 else 0
print(f'Rabat wynosi {rabat}')

lista_bledow = []
alert_system = 'email'
error = 'nieznany'
error_message = "Stało sie coś strasznego"

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    if error == 'medium':
        lista_bledow.append("ostrzeżenie")
    elif error == 'critical':
        lista_bledow.append('krytyczny')
    else:
        lista_bledow.append('inny')
print(lista_bledow)

# zrobic test z historii
# wyswietlic pytanie
# pobrac odpowiedz
# zweryfikowac odpowiedz
# wyswietlic komunikat w zaleznosci od odpowiedzi
odp = input("Podaj date chrztu Polski")
if odp == "966":
    print("Brawo")
else:
    print("Maszw książce na 23 stronie")