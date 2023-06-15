from dataclasses import dataclass
import pickle


@dataclass  # oznacza klasa danych, python automatycznie wygeneruje niektore elementy
class Person:
    first_name: str
    last_name: str
    id: int

    def greet(self):
        print(f"Witam, jestem {self.first_name} {self.last_name}, Id to {self.id}")


# kod z tego ifa wykona sie tylko gdy ten plik bedzie uruchomiony bezpośrednio
if __name__ == '__main__':
    p1 = Person("Jacek", "Kowalski", 1)
    print(p1)  # Person(first_name='Jacek', last_name='Kowalski', id=1)
    p1.greet()
    # Witam, jestem Jacek Kowalski, Id to 1
    people = [
        Person("Jacek", "Kowalski", 1),
        Person("Mateusz", "Zegar", 2)
    ]
    print(people)
    print(people[0])  # Person(first_name='Jacek', last_name='Kowalski', id=1)

    with open('data.pickle', 'wb') as stream:
        pickle.dump(people, stream)
