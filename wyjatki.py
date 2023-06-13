# while True- kalkulator
while True:
    print("""
    1. Dodawwanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec""")

    odp = input("Podaj działanie jakie chcesz wykonać")
    if odp == '5':
        break
    try:
        a = int(input("Podaj pierwszą liczbę"))
        b = int(input("Podaj drugą liczbę"))

        if odp == '1':
            print(f"wynik dodawania {a} + {b} = {a + b}")
        elif odp == '2':
            print(f"wynik odejmowania {a} - {b} = {a - b}")
        elif odp == '3':
            print(f"wynik mnożenia {a} * {b} = {a * b}")
        elif odp == '4':
            print(f"wynik dzielenia {a} / {b} = {a / b}")
        else:
            print("Nie znam takiego działania")
    except ZeroDivisionError:
        print(f"Nie dziel przez zero")
    except ValueError:
        print("Bład wartości")
    except TypeError:
        print("Błąd typu")
    except Exception as e:
        print("Bład", e)
    else:
        print("Gdy nie ma błedu")
    finally:
        print("Zawsze")
# dorobic mnozenie i dzielenie
# wynik dzialania a + b = wynik
# ZeroDivisionError: division by zero
