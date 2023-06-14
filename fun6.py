# argumenty słownikowe
def connect(**opcje):
    print(opcje)
    print(type(opcje))  # <class 'dict'>
    connect_param = {
        'host': '127.0.0.7',
        'port': '8080'
    }
    print(connect_param)  # {'host': '127.0.0.7', 'port': '8080'}
    connect_param['pwd'] = opcje
    print(connect_param)
    # {'host': '127.0.0.7', 'port': '8080', 'pwd': {'name': 'Radek'}}
    connect_param.update({'pwd2': opcje})
    print(connect_param)
    # {'host': '127.0.0.7', 'port': '8080',
    #  'pwd': {'name': 'Radek'},
    #  'pwd2': {'name': 'Radek'}}


# connect(1,2)
# TypeError: connect() takes 0 positional arguments but 2 were given
connect()  # {}
connect(name="Radek")  # {'name': 'Radek'}
connect(a=9, b=9)
connect(radek='Test', host='/')
