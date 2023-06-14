import csv
filename = 'records.csv'

fields = []
rows = []

with open(filename,'r') as csv_f:
    csvreader = csv.reader(csv_f)
    print(type(csvreader))  # <class '_csv.reader'>

    fields = next(csvreader)
    # next - odczyta biezaca daną (tu indeks 0) i ustawi wskaźnik odczytu na kolejny (tu na indeks 1)

    for row in csvreader:
        rows.append(row)

print(fields)
print(rows)