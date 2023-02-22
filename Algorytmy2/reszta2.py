T = [50,20,10,5,2,1]
T.sort(reverse=True)
W = []
x = int(input("Reszta: "))
for i in T:
    ilość = x // i
    if ilość > 0:
        x = x - ilość * i
        for j in range(ilość):
            W.append(i)
print(W)