import math

potenze = True
n = int(input())

while n != 0:
    log2 = round(math.log(n, 2))
    if 2**log2 != n:
        potenze = False

    n = int(input())

if potenze:
    print("SI", end='')
else:
    print("NO", end="")
