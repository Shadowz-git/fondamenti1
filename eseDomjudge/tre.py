indice = -1
numeri = []


def main() -> None:
    x = int(input())
    for i in range(1, x + 1):
        numeri.append(i)
    mat = creaMatrice(10, 10)
    print(calcDiagSec(mat), end="")


def calcDiagSec(mat: list) -> int:
    somma = 0
    lungMat = len(mat)
    for i in range(lungMat):
        somma += mat[i][lungMat - 1 - i]

    return somma


def creaMatrice(r: int, c: int) -> list:
    m = []

    for i in range(r):
        m.append([])
        for j in range(c):
            m[i].append(getValori())

    return m


def getValori() -> int:
    global numeri
    global indice
    if indice == len(numeri) - 1:
        indice = 0
    else:
        indice += 1

    return numeri[indice]


main()
