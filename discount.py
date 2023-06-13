from datetime import date, timedelta, datetime

today = date.today()
print(today)  # 2023-06-13

time = datetime.now()
print(time)  # 2023-06-13 14:30:35.968537

print(type(time))  # <class 'datetime.datetime'>

# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tommorow = today + timedelta(days=1)
print(tommorow)  # 2023-06-14

print(time.hour)
print(today.day)

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': tommorow, 'price': 50.0},
    {'sku': 3, 'exp_date': today, 'price': 25},
]

print(products)

for product in products:
    print(product)
    print(type(product))  # <class 'dict'>
    if product['exp_date'] != today:  # różne
        continue  # wroci na poczatek pętli
    product['price'] *= 0.8  # p = p * 0.8
    print(f"""
    Price for sku = {product['sku']}
    is now {product['price']}
""")
