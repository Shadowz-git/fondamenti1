def main() -> None:
    n = int(input())
    mat = creaMatrice(n, n)
    ok = controlloMatrice(mat)
    if ok:
        print('SI', end='')
    else:
        print('NO', end='')


def creaMatrice(r: int, c: int) -> list:
    m = []
    for i in range(r):
        m.append([])
        for j in range(c):
            m[i].append(int(input()))

    return m


def controlloRiga(mat: list, riga: int) -> bool:
    l = []
    for i in range(len(mat[riga])):
        if l.count(mat[riga][i]) == 0:
            l.append(mat[riga][i])
        else:
            return False

    return True


def controlloColonna(mat: list, colonna: int) -> bool:
    l = []
    for i in range(len(mat)):
        if l.count(mat[i][colonna]) == 0:
            l.append(mat[i][colonna])
        else:
            return False

    return True


def controlloMatrice(mat: list) -> bool:
    for i in range(len(mat)):
        if not controlloRiga(mat, i) or not controlloColonna(mat, i):
            return False

    return True


main()
