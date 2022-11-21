# sprawdz czy dana liczba jest pierwsza

n = int(input())
for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        print("NIE JEST PIERWSZA")
        exit()

print("TAK, LICZBA JEST PIERWSZA")
