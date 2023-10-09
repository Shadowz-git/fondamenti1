def main():
    righe = int(input())
    colonne = int(input())
    M = matrice(righe, colonne)
    giudiceBuono = controlloGiudiceBuono(M)
    cantanteScarso = controlloCantanteScarso(M)
    print(giudiceBuono, cantanteScarso, end='')


def matrice(r, c):
    M = []
    for i in range(r):
        M.append([])
        for j in range(c):
            M[i].append(int(input()))

    return M


def controlloGiudiceBuono(mat):
    index = 0
    somma = 0
    maxi = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] > 5:
                maxi += 1

        if maxi >= somma:
            somma = maxi
            index = i
        maxi = 0

    return index


def controlloCantanteScarso(mat):
    somma = 0
    minimo = 10000
    index = 0
    for j in range(len(mat[0])):
        for i in range(len(mat)):
            somma += mat[i][j]

        if somma <= minimo:
            minimo = somma
            index = j
        somma = 0

    return index


main()
