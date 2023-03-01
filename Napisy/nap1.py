# napis jest jest prawie "listą"
# s = input()
# print(s)

# for i in s:
#     print(i)
# for i in range(len(s)):
#     print(s[i])

# L = [5,7,2,4]
# print(L)
# L.sort()
# print(L)
# s = input()
# print(s)
# s.sort() - to jest błąd, napis to nie normalna lista
# print(s)

# przechodzenie: napis <-> lista (list() i join())

# s = input()
# L = list(s)
# print(s, L)
# L.sort()
# print(s, L)
# s = "".join(L)
# print(s, L)

# napisz alg który sprawdzi czy wyraz jest palindromem

# s = input()
# L = list(s)
# R = L.copy()  # R = list(s)
# R.reverse()
# if L == R:
#     print("TAK")
# else:
#     print("NIE")

# palindrom ver 2
s = input()
for i in range(len(s)//2):
    if s[i] != s[len(s)-1-i]:
        exit("NIE")
exit("TAK")
