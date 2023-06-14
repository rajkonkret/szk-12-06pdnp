# funkcja do oblicznia średniej

a, *b = 1, 2, 3


def liczby(i=0, *cyfry):
    suma = 0
    print(cyfry)  # (1, 2, 3, 4)
    print(type(cyfry))  # <class 'tuple'>
    for cy in cyfry:
        print(cy)
        suma += cy
    print(f"Suma {suma}")
    count = len(cyfry)
    try:
        print(f"Średnia wynosi {suma / count} dla ucznia numer {i}")
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except Exception as e:
        print("Bład", e)


liczby(1, 2, 3, 4)
liczby()
liczby(5, 6, 7, 8, 9, 3, 4, 5, 6, 2, 2, 1, 1, 1, 3, 4, 4, 6, 6, 5, 6, 7, 8, 5)
