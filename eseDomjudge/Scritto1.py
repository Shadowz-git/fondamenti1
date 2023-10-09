terzaCondizione = True

def main() -> None:
    n = int(input())
    m = int(input())
    a = int(input())
    mat = creaMatrice(n, m)
    totAlberi = totaleAlberi(mat, a)
    casePiuAlberi = caseMaggioreAlberi(mat)
    if totAlberi and casePiuAlberi and terzaCondizione:
        print('OK', end="")
    else:
        print('NO', end='')


def alberiSuRiga(mat:list, index: int) -> int:
    alberi = 0
    if index >= len(mat) or index < 0:
        return alberi
    for i in range(len(mat[index])):
        if mat[index][i] == "*":
            alberi += 1

    return alberi


def caseSuRiga(mat: list, index: int) -> int:
    global terzaCondizione
    case = 0
    if index >= len(mat) or index < 0:
        return case
    for i in range(len(mat[index])):
        if not mat[index][i] == "*" and int(mat[index][i]) > 0:
            if not alberiAdiacenti(mat, index, i):
                terzaCondizione = False
            case += 1

    return case


def alberiAdiacenti(mat: list, riga: int, colonna: int) -> bool:
    alberiVicini = 0
    alberi = int(mat[riga][colonna])
    if not (riga - 1 < 0):
        if mat[riga - 1][colonna] == "*":
            alberiVicini += 1
        if not (colonna - 1 < 0):
            if mat[riga - 1][colonna - 1] == "*":
                alberiVicini += 1
        if not (colonna + 1 >= len(mat[riga])):
            if mat[riga - 1][colonna + 1] == '*':
                alberiVicini += 1
    if not (riga + 1 >= len(mat)):
        if mat[riga + 1][colonna] == "*":
            alberiVicini += 1
        if not (colonna - 1 < 0):
            if mat[riga + 1][colonna - 1] == "*":
                alberiVicini += 1
        if not (colonna + 1 >= len(mat[riga])):
            if mat[riga + 1][colonna + 1] == "*":
                alberiVicini += 1
    if not (colonna - 1 < 0):
        if mat[riga][colonna - 1] == "*":
            alberiVicini += 1
    if not (colonna + 1 >= len(mat[riga])):
        if mat[riga][colonna + 1] == "*":
            alberiVicini += 1

    return alberiVicini == alberi


def totaleAlberi(mat: list, alberi: int) -> bool:
    alberiTot = 0

    for i in range(len(mat)):
        alberiTot += alberiSuRiga(mat, i)

    return alberiTot == alberi


def caseMaggioreAlberi(mat: list) -> bool:
    for i in range(len(mat)):
        alberi = alberiSuRiga(mat, i)
        case = caseSuRiga(mat, i)
        if alberi > case:
            return False
    return True


def creaMatrice(r: int, c: int) -> list:
    m = []

    for i in range(r):
        m.append([])
        for j in range(c):
            m[i].append(input())

    return m


main()
