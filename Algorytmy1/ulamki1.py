a = int(input())
b = int(input())
c = int(input())
d = int(input())

x, y = b, d
ilocz = x * y
while y > 0:
    x, y = y, x % y
nww = ilocz // x

e = (nww // b) * a
f = (nww // d) * c
g = e + f

print(f"{a}/{b} + {c}/{d} = {e}/{nww} + {f}/{nww} = {g}/{nww}")