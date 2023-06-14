# plik csv - dane oddzielone znakiem podziału
# Radek,Maciek,Zenek

import csv

fields = ['name', 'branch', 'year', 'cgpa']
# ['radek', 'COE','3','9']
my_list_dict = [
    {'branch': 'COE', 'cgpa': '9.1', 'year': 2, 'name': 'Radek'},
]

filename = 'records.csv'

with open(filename, 'w', newline='') as csv_f:
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerows(my_list_dict)