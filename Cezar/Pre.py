# Funkcja ord() - zwraca kod ascii danego znaku
# print(ord("A"))
# print(ord("B"))
# print(ord("Z"))

# Funkcja chr() - zwraca znak danego kodu ascii
# print(chr(65))
# print(chr(75))
# print(chr(89))

# znaki ASCII od A-Z mają kody 65-90 !!!!!!!!

# wypiszcie pętla for cały alfabet A-Z

# for i in range(65,91):
#     print(chr(i), end="")

# jak słowo rozbić na litery...?

napis = "MAREK"
szyfr = ""
# print(len(napis))  # zwraca długość napisu
# print(napis[0])    # napis to lista
# print(napis[1])    
# print(napis[2])

# wypiszcie kody ASCII literek napisu
for i in range(len(napis)):
    szyfr = szyfr + chr(65 + (ord(napis[i])-65+3) % 26)
print(napis)
print(szyfr)
