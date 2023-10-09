numeri = int(input())
div = False

while numeri != 5:
    if numeri % 5 == 0:
        div = True
    numeri = int(input())

if div:
    print("ALMENO 1", end="")
else:
    print("NESSUNO", end="")
