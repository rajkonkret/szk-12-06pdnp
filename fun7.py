def allparams(a, b, /, c=42, *args, d=256, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print("args", args)
    print("kwargs", kwargs)


allparams(1, 2)
# allparams(b=6, a=4)
# TypeError: allparams() missing 2 required positional arguments: 'a' and 'b'
allparams(1, 2, c=8)
allparams(1, 2, 8, 4, 5, 6, 7, 8, 9, 0, d=4)
allparams(1, 2, 8, 4, 5, 6, 7, 8, 9, 0, d=4, e=8)  # kwargs {'e': 8}
allparams(1, 2, 8, 4, 5, 6, 7, 8, 9, 0, a=9, d=4, e=8)  # kwargs {'e': 8}
