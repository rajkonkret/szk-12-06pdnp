wiek = 47
rok = 2023
temp = 36.6
wiek2 = 37.5  # <class 'float'>

print(wiek2)
print(type(wiek2))  # <class 'float'>

print(5 * "Radek")  # RadekRadekRadekRadekRadek

print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)  # 0.023232822540781017 zawsze zwraca float
print(wiek // rok)  # dzielenie całkowite - czesc całkowita
print(wiek % rok)  # modulo, czyli reszta z dzielenia
print(wiek ** rok)  # potęgowanie
print(5 % 2)  # reszta z dzielenia 1
print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - (5 * 43) + (4 / 2 + 4) / 2)  # -158.0
print(0.2 + 0.8)
print(0.2 + 0.7)  # 0.8999999999999999
wynik = 0.2 + 0.7
print(f"{wynik:.1f}")  # 0.9
print(wynik)  # 0.8999999999999999

print(f"\tSprawdzenie zmiennej temp {wiek} {temp}")
print(f"""
    {wiek}
    {temp}
""")

print(type(4 / 2))  # <class 'float'>
print(type(4 // 2))  # <class 'int'>

# typ logiczny
print("True/False")
czy_znasz_pythona = True
print(czy_znasz_pythona)
print(type(czy_znasz_pythona))  # <class 'bool'>
print(int(czy_znasz_pythona))  # rzutowanie na int czyli na typ liczbowy
print(int(False))
# 1 True - wszystko rózne od zera jest True
# 0 False
x = 1
print(bool(x))
x = 100
print(bool(x))  # True
x = -10
print(bool(x))  # True

print(bool("radek"))
print(bool(""))  # False

a = 14
b = 3
print(f"wynik porównania {a} > {b}", a > b)
print(f"wynik porównania {a} < {b}", a < b)
print(f"wynik porównania {a} == {b}", a == b)  # == - porównnie
print(f"wynik porównania {a} != {b}", a != b)  # różne
