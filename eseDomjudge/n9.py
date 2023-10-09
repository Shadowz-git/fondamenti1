n = int(input())
cont = 0

while n != 0:
    if (n % 2 != 0) and (n % 3 == 0):
        cont += 1
    n = int(input())

print(cont, end="")