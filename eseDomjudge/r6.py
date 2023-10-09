def main():
    N = int(input())
    M = matrice(N, N)
    ricorsione = ricorsivaL(M, len(M)-1, 0)
    if ricorsione:
        print(ricorsione, end='')
    else:
        print('NO', end='')


def matrice(r, c):
    mat = []
    for i in range(r):
        mat.append([])
        for j in range(c):
            mat[i].append(int(input()))

    return mat


def sommaRigaDaColonna(mat, r, c):
    somma = 0
    for i in range(c, len(mat[r])):
        somma += mat[r][i]

    return somma


def sommaColonnaDaRiga(mat, c, r):
    somma = 0
    for i in range(r, -1, -1):
        somma += mat[i][c]

    return somma


def ricorsivaL(mat, r, c):
    if c >= len(mat[0]) or r < 0:
        return "SI"
    sommaR = sommaRigaDaColonna(mat, r, c)
    sommaC = sommaColonnaDaRiga(mat, c, r)
    somma = sommaR + sommaC - mat[r][c]
    if somma % mat[r][c] == 0:
        return ricorsivaL(mat, r-1, c + 1)


main()
