from xml.dom import minidom

DOMTree = minidom.parse('dane_xml.xml')

print(DOMTree.toxml())

cNodes = DOMTree.childNodes
print(cNodes)  # [<DOM Element: znajomi at 0x100224550>]
print(cNodes[0].getElementsByTagName('osoba')[0].toxml())
print(cNodes[0].getElementsByTagName('osoba')[1].toxml())
print(cNodes[0].getElementsByTagName('osoba')[1].getElementsByTagName('imie'))
# [<DOM Element: imie at 0x102e58230>]
print(cNodes[0].getElementsByTagName('osoba')[1].getElementsByTagName('imie')[0].toxml())
# <imie foo="aaaa">Janina</imie>

