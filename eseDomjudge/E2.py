def main():
    N = int(input())
    M = matrice(N, N)
    C = valori(N)
    R = valori(N)
    risolto = organigramma(M, R, C)
    if risolto:
        print("SI", end='')
    else:
        print("NO", end='')


def matrice(r, c):
    mat = []
    for i in range(r):
        mat.append([])
        for j in range(c):
            mat[i].append(int(input()))

    return mat


def valori(n):
    l = []
    for i in range(n):
        l.append(int(input()))

    return l


def countRiga(mat: list, index: int, colonna: bool = False) -> int:
    count = 0
    trovato = False
    if colonna:
        for i in range(len(mat)):
            if mat[i][index] == 1:
                trovato = True
                count += 1

            elif mat[i][index] == 0:
                if trovato and count == 0:
                    return -1
                elif trovato and count > 0:
                    return count
    else:
        for i in range(len(mat[0])):
            if mat[index][i] == 1:
                trovato = True
                count += 1
            elif mat[index][i] == 0:
                if trovato and count == 0:
                    return -1
                elif trovato and count > 0:
                    return count

    return count


def organigramma(mat: list, r: list, c: list) -> bool:
    for i in range(len(mat)):
        if countRiga(mat, i) != r[i]:
            return False

    for i in range(len(mat[0])):
        if countRiga(mat, i, True) != c[i]:
            return False

    return True

main()
