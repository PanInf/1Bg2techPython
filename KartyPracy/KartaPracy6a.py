# Zad 1

# n = int(input())
# suma = 0
# while n > 0:
#     cyfra = n % 10 
#     suma = suma + cyfra
#     n = n // 10
# print(suma)

# Zad 2 

# wersja 1
# n = int(input())
# flaga = True
# for i in range(2,n):
#     if n % i == 0:
#         flaga = False
#         break
# if flaga == True:
#     print("TAK")
# else:
#     print("NIE")

# wersja 2
# n = int(input())
# for i in range(2,n):
#     if n % i == 0:
#         print("NIE")
#         exit(0)
# print("TAK")

# wersja 3
# n = int(input())
# suma = 0
# for i in range(2,n):
#     if n % i == 0:
#         suma = suma + i
# if suma == 0:
#     print("TAK")
# else:
#     print("NIE")
