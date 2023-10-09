X = int(input())
lista = []
crescente = True
dispari = True

for y in range(X):
    lista.append(int(input()))

for x in range(2, len(lista), 2):
    if lista[x-2] >= lista[x]:
        crescente = False

for i in range(1, len(lista), 2):
    if lista[i] % 2 == 0:
        dispari = False

if crescente and dispari:
    print("SI", end='')
else:
    print("NO", end='')
    