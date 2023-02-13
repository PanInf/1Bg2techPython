# PRE

# from math import gcd
# print(gcd(15,20))

# 1. Wybór 2 dużych liczb pierwszych
p = 101
q = 97
print(p,q)

# 2. Liczmy n = p*q oraz funkcje Eulera F = (p-1) * (q-1)
n = p * q
F = (p-1) * (q-1)
print(n)
print(F)

# 3. Generujemy klucz publiczby e taki, że NWD(F,e) = 1
from math import gcd
for i in range(2,F):
    if gcd(i,F) == 1:
        e = i
        break
print(e, n)

# 4. Generujemy klucz prywatny d : d*e mod F == 1
for j in range(2,F):
    if ((j*e) % F) == 1:
        d = j
        break
print(d,n)

# 5. Przykład jak szyfrować?
# mamy m - message - wiadomość
# c = m**e % n (c - cipher - szyfrogram, tekst zaszyfrowany)
# t = c**d % n (t - text - tekst jawny - znów wiadomość m)

m = input()
cipher = ""
for i in m:
    cipher += chr((ord(i)**e)%n)

print(m)
print(cipher)

tekst =""
for i in cipher:
    tekst += chr((ord(i)**d)%n)
print(tekst)