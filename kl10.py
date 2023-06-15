class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print('Jadę pojazdem')


class Car(Vehicle):
    def drive(self):
        print('Jazdę samochodem')


class Bike(Vehicle):
    def drive(self):
        print('Jade rowerem')


class HybridCar(Car, Bike):
    def drive(self):
        super().drive()
        Bike.drive(self)
        print("Jadę samochodem hybrydowym")


# stworzyc obiekty dla tych trzech klas i uzyc nanich metody drive()

car1 = Car("Polonez")
car1.drive()

rower = Bike("Giant")
rower.drive()

hyb = HybridCar("Toyota")
hyb.drive()
print(HybridCar.__mro__)
# (<class '__main__.HybridCar'>,
# <class '__main__.Car'>, <class '__main__.Bike'>,
# <class '__main__.Vehicle'>, <class 'object'>)
