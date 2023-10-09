n = int(input())
vuota = True
L = []
stringa = ""
cont = 0
Liste = []
passato = True
massima = 0

while n >= 0:
    L.append(n)
    n = int(input())
    vuota = False

if not vuota and len(L) > 1:
    for x in range(len(L)-1):
        if L[x] <= L[x+1] and passato:
            Liste.append([x])
            passato = False
        elif L[x] > L[x+1]:
            passato = True
            while len(Liste) <= cont:
                Liste.append([x])
            Liste[cont].append(x)
            cont += 1
        if x+1 == len(L)-1 and L[x] <= L[x+1]:
            Liste[cont].append(x+1)
        elif x+1 == len(L)-1 and L[x] > L[x+1]:
            Liste.append([x+1])

    cont = 0
    for i in Liste:
        if (len(i) > 1) and ((i[1] - i[0]) > massima):
            massima = cont

        cont += 1

    cont = 0
    for i in L[Liste[massima][0]:Liste[massima][1]+1]:
        cont += 1
        print(i, end='')
    print()
    print(cont, end="")
elif len(L) == 1:
    print(L[0])
    print(1, end="")

if vuota:
    print("Empty", end="")