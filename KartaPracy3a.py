# Zad 1
# n = int(input())
# for i in range(n):
#     print("*-|", end="")

# PRE1
# print(5+6)
# print("Bartosz"+"Nowak")
# # print("Bartosz"+5)
# print("Bartosz"*5)

# n = int(input())
# print("*-|"*n)

# Zad 2
# n = int(input())
# for i in range(1, n+1):
#     print("*"*i, end="")
#     if i % 2 == 1:
#         print("||", end="")
#     else:
#         print("--", end="")

# Zad 3
n = int(input())
for i in range(1, n+1):
    print("*", end="")
    if i % 2 == 0:
        print("-"*i, end="")
    else:
        print("|"*i, end="")




