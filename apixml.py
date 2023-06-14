import requests
import xml.etree.ElementTree as ET

url = 'http://api.nbp.pl/api/exchangerates/tables/A?format=xml'

response = requests.get(url)
print(response)  # <Response [200]>

xml_data = response.content

print(xml_data)

root = ET.fromstring(xml_data)
print(root)
table_name = root.find('.//Table').text
print(f"Tabela: {table_name}")  # Tabela: A

date = root.find('.//EffectiveDate').text
print(date)  # 2023-06-14
rates = root.findall('.//Rate')

print(rates)

for rate in rates:
    currency = rate.find('Currency').text
    code = rate.find('Code').text
    mid = rate.find('Mid').text
    print(f"{code}: {currency} - {mid}")
