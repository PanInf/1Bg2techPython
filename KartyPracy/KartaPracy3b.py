# Zad 8

L = float(input("Podaj długość trwania inwestycji: "))
W0 = int(input("Podaj ile kasy wrzucasz na inwestycje: "))
W = W0
for i in range(int(L*12)):
    W = W*(1+(0.5)/100)
print(W)
