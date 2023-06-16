numbers = [1, 2, 3, 4, 5]

# Tworzenie nowej listy
squared = [num ** 2 for num in numbers]
print(f"Squared: {squared}")  # Squared: [1, 4, 9, 16, 25]

# for num in numbers:
#     jakaslista.append(num)

even_numbers = [num for num in numbers if num % 2 == 0]
print(f"Parzyste: {even_numbers}")  # Parzyste: [2, 4]

modifed_numbers = [num * 2 if num % 2 == 0 else num for num in numbers]
print(f"Zmodyfikowane: {modifed_numbers}")

even_odd = ['parzysta' if x % 2 == 0 else 'nieparzysta' for x in numbers]
print(f"parzyste-nieparzyste {even_odd}")
# parzyste-nieparzyste ['nieparzysta', 'parzysta', 'nieparzysta', 'parzysta', 'nieparzysta']

squared_numbers = [x ** 2 for x in range(1, 6)]  # 1..5
print(f"Kwadrat liczb z zakresu: {squared_numbers}")
# Kwadrat liczb z zakresu: [1, 4, 9, 16, 25]

# abs() - wartośc absolutna - liczby bez znaku
numbers2 = [-1, -2, 3, -4, 5]
absolute = [abs(x) for x in numbers2]
print(f"Wartosci absolutne z listy: {absolute}")
# Wartosci absolutne z listy: [1, 2, 3, 4, 5]

word = "Python"
letters = [letter for letter in word]
print(f"Literki: {letters}")
# Literki: ['P', 'y', 't', 'h', 'o', 'n']

lista1 = [word]
print(lista1)  # ['Python']

print(list(word))  # ['P', 'y', 't', 'h', 'o', 'n']
