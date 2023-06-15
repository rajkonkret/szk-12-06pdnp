# wielodziedziczenie
class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("Metoda z klasy B")


class C(B, A):
    """
    klasa C - dziedziczy po klasie A i B
    """

    def method(self):
        # print("Metoda z klasy C")
        # super().method()
        A.method(self)
        print("Cos dodatkowego")


a = A()
a.method()

b = B()
b.method()

c = C()
c.method()
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
# https://www.onlinegdb.com