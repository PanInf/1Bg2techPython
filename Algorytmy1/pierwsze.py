# 1. Sprawdzenie czy liczba jest pierwsza
# liczba pierwsza - liczba, która się dzieli tylko przez 1 i samą siebie
# 2,3,5,7,11,13,17,19,23 .. itd
# dzielniki właściwe - dzielniki liczby poza 1 i nią samą

# n = int(input())
# for i in range(2, n):
#     if n % i == 0:
#         print("Liczba nie jest pierwsza")
#         exit(0)
# print("Liczba jest pierwsza")

# 2. Generowanie liczb pierwszych (w przedziale [p,q])

# p, q = int(input()), int(input())

# for j in range(p, q+1):
#     flaga = True
#     for i in range(2, j):
#         if j % i == 0:
#             flaga = False
#             break
#     if flaga == True:
#         print(j, end=" ")

# 3. Generowanie liczb pierwszych (pierwsze n liczb pierwszych)

n = int(input("Podaj ile chcesz liczb pierwszych: "))

k = 2
ilosc = 0
while 1:
    flaga = True
    for i in range(2, k):
        if k % i == 0:
            flaga = False
            break
    if flaga == True:
        print(k, end=" ")
        ilosc = ilosc + 1
    if ilosc == n:
        break
    k = k + 1
