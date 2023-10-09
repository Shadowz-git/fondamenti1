X = int(input())
N = int(input())

cont = 0
i = 1
while i <= N:
    if i % X == 0:
        cont += 1
    i += 1
print(cont, end="")