from kl13 import Person
import pickle

with open('data.pickle', 'rb') as file:
    p = pickle.load(file)

print(p)
# [Person(first_name='Jacek', last_name='Kowalski', id=1), Person(first_name='Mateusz', last_name='Zegar', id=2)]

print(p[0])  # Person(first_name='Jacek', last_name='Kowalski', id=1)

for person in p:
    person.greet()
# Witam, jestem Jacek Kowalski, Id to 1
# Witam, jestem Mateusz Zegar, Id to 2
