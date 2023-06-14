import requests as re

url = 'http://api.nbp.pl/api/exchangerates/rates/A/EUR/'
response = re.get(url)
print(response)
# <Response [200]> ok
# 3xx - rozne
# 4xx - 404 - brak zasobu, 400 bad request
# 5xx - błedy wewnętrzne serwera
table = response.json()
print(table)
# {'table': 'A', 'currency': 'euro', 'code': 'EUR',
#  'rates': [{'no': '112/A/NBP/2023', 'effectiveDate': '2023-06-13', 'mid': 4.4783}]}
print(table['table'])
print(table['rates'][0])
# {'no': '112/A/NBP/2023', 'effectiveDate': '2023-06-13', 'mid': 4.4783}
print(table['rates'][0]['mid'])  # 4.4783
print(table['rates'][0]['effectiveDate'])  # 2023-06-13


