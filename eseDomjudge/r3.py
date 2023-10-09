def main():
    n = int(input())
    M = matrice(n, n)
    ricorsiva = sommaDiagSecRe(M, 0)
    iterativa = sommaDiagSecIt(M)
    print(str(iterativa)+";"+str(ricorsiva), end="")

def matrice(r, c):
    mat = []
    for i in range(r):
        mat.append([])
        for j in range(c):
            mat[i].append(int(input()))

    return mat


def sommaDiagSecRe(mat, x):
    if x == len(mat):
        return 0
    return mat[x][-x-1] + sommaDiagSecRe(mat, x + 1)


def sommaDiagSecIt(mat):
    somma = 0
    for i in range(len(mat)):
        somma += mat[i][-i-1]

    return somma


main()
