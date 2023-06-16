import os

for root, dirs, files in os.walk(".."):
    abs_root = os.path.abspath(root)
    print(abs_root)
    if dirs:
        print("Directories")
        for dir_ in dirs:
            print(dir_)

    if files:
        print("files")
        for filename in files:
            print(filename)

print(os.path.abspath('Catalog.xml'))
# /Users/radoslawjaniak/PycharmProjects/szk-12-06pdnp/Catalog.xml
