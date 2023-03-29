# ZAGADNIENIA Napisy 
# - len, for, "foreach", ord, chr
# - indeksy, zakresy
# - konwersje list <-> napis
# - list - sort reverse
# - split, join
# Algorytmy - anagram, palindom, Boyer-Moore

# Wszystkie zadania wykonujemy na 26-znakowym
# alfabecie maturalnym: od A (65) do Z (90)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

# Przykładowe zadania:

# 1. Wczytaj dowolny napis i wypisz z niego pierwszą i ostatnią literkę

# a = input()
# print(a[0], a[-1])
# print(a[0], a[len(a)-1])

# 2. Wczytaj dowolny napis i wypisz z niego literki bez pierwszej i ostatniej

# b = input()
# for i in range(1, len(b)-1):
#     print(b[i], end="")
# print()

# print(b[1:len(b)-1])

# print(b[1:-1])

# L = list(b)
# L.pop(0)
# L.pop(-1)
# b = "".join(L)
# print(b)

# 3. Wypisz 4 ostatnie literki z wpisanego napisy w kolejności od końca

# c = input()

# print(c[-1:-5:-1])

# for i in range(len(c)-1,len(c)-5,-1):
#     print(c[i], end="")
# print()

# L = list(c)
# L.reverse()
# c = "".join(L)
# print(c[:4])

# 4. Waga napisu to suma kodów ascii jego liter. Zważ wpisny napis

# d = input()
# s = 0
# for x in d:
#     s += ord(x)
# znak = s // len(d)
# print(chr(znak))

# 5. Policz ile we wpisanym napisie jest liter A.

# e = input()
# ilosc = 0
# for x in e:
#     if x == "A":
#         ilosc += 1
# print(ilosc)

# SAMO = ["A", "E", "I", "O", "U", "Y"]

# ilosc_samo = 0
# for x in e:
#     if x in SAMO:
#         ilosc_samo += 1
# print(ilosc_samo)


# 6. Podaj dominującą literkę we wpisanym napisie. 
# Niech to będzie tylko jedna literka.

# f = input()
# maksiu = 0
# for x in f:
#     if f.count(x) > maksiu:
#         maksiu = f.count(x)
#         literka = x
# print(literka, maksiu)

# 7. Znajdź literkę-dominantę w napisie (może ich być kilka, a może nie być żadnej)

# 8. Sprawdź czy w napisie występują trzy podciągi "LA"

h = input()
ilosc = 0
for i in range(len(h)):
    # if h[i:i+2] == "LA":
    # if h[i] == "L" and h[i+1] == "A":
    if h[i] + h[i+1] == "LA":
        ilosc += 1
if ilosc == 3:
    print("TAK")
else:
    print("NIE")
    

# 9. Znajdź "średnią literkę" w napisie. (Przejdź na kody ASCII i jeśli wynik będzie
# ułamkowy to zaokrąglij średnią w dół)

# 10. Wypisz literki, których nie ma w napisie

# 11. Znajdź ilość trzyznakowych palindromów w napisie (trzy literki koło siebie)
