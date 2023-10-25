X = int(input())
N = int(input())
cont = 0
numeri = ""

while cont < N:
    a = int(input())
    cont += 1
    if a % 2 == 0 and a < X:
        numeri += str(a)

if len(numeri) > 0:
    print(numeri, end="")
4
2019
2
2021
3
2021
0
2019
3
1980
