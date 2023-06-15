class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    raise MyException("wystąpił wyjątek")
# Traceback (most recent call last):
#   File "/Users/radoslawjaniak/PycharmProjects/szk-12-06pdnp/kl11.py", line 6, in <module>
#     raise MyException("wystąpił wyjątek")
# MyException: wystąpił wyjątek
except MyException:
    print("wystąpił wyjątek MyException")
# wystąpił wyjątek MyException
