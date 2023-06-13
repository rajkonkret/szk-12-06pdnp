tekst = "Witaj świecie"
print(tekst)  # Witaj świecie
tekst2 = tekst.upper()
print(tekst)
print(tekst2)  # WITAJ ŚWIECIE
tekst3 = tekst2.lower()
print(tekst)  # Witaj świecie
print(tekst3)  # witaj świecie
print(tekst.upper())  # WITAJ ŚWIECIE
print(tekst)  # Witaj świecie

print(tekst.removeprefix("Witaj"))  # " świecie"
print(tekst)
print(tekst.removesuffix("świecie"))  # "Witaj "
print(tekst)  # Witaj świecie

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie'
tekst_bajtowy = b"To jest tekst bajtowy"
print(tekst_bajtowy)
print(type(tekst_bajtowy))  # <class 'bytes'>
print(encoded_s.decode('utf-8'))  # Witaj świecie

print(tekst.count("i"))
print(tekst.count("i", 0, 4))  # od 0..3 włącznie
imie = "Radek"
tekst_format = f"Mam\t na imię {imie} \n i lubię \bPythona"
print(tekst_format)

# \t tabulator
# \n nowa linia
# \b  backspace

starszy = "Witaj %s!"
print(starszy % imie)  # Witaj Radek!
print("Witaj {}!".format(imie))
print("""
Tekst wielolinijkowy
    druga linia
    
    """)
# Tekst wielolinijkowy
# druga linia

# ctrl - /(?) - komentarz zanzaczonych linijek

