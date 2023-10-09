def main() -> None:
    N = int(input())
    M = int(input())

    mat = creaMatrice(N, M)

    if N % 2 != 0 or M % 3 != 0 or not bombe(mat):
        print('NO', end='')
    else:
        print('SI', end='')


def creaMatrice(r: int, c: int) -> list:
    l = []
    for i in range(r):
        l.append([])
        for j in range(c):
            l[i].append(int(input()))

    return l


def bombe(lista: list) -> bool:
    primoSettore = 0
    secondoSettore = 0
    terzoSettore = 0
    quartoSettore = 0

    suddivisioneColonne = len(lista[0])//3
    suddivisioneRighe = len(lista)//2

    for i in range(len(lista)):
        for j in range(len(lista)//3):
            if lista[i][j] == 0:
                primoSettore += 1

    for i in range(0, suddivisioneRighe):
        for j in range(suddivisioneColonne, suddivisioneColonne*2):
            if lista[i][j] == 0:
                secondoSettore += 1

    for i in range(suddivisioneRighe, len(lista)):
        for j in range(suddivisioneColonne, suddivisioneColonne*2):
            if lista[i][j] == 0:
                terzoSettore += 1

    for i in range(len(lista)):
        for j in range(suddivisioneColonne*2, len(lista[0])):
            if lista[i][j] == 0:
                quartoSettore += 1

    return primoSettore == 1 and secondoSettore == 1 and terzoSettore == 1 and quartoSettore == 1



main()