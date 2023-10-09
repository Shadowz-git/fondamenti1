def main() -> None:
    N = int(input())
    M = int(input())

    mat = creaMatrice(N, M)
    bombe = cercaBombe(mat)
    if bombe:
        print('SI', end='')
    else:
        print('NO', end='')


def creaMatrice(r: int, c: int) -> list:
    l = []
    for i in range(r):
        l.append([])
        for j in range(c):
            l[i].append(int(input()))

    return l


def cercaBombe(mat: list) -> bool:
    lunRighe = len(mat)
    lunColonne = len(mat[0])
    contRighe = 0
    contColonne = 0

    for i in range(lunRighe):
        rigaAttuale = 0
        for j in range(lunColonne):
            if mat[i][j] == 0:
                rigaAttuale += 1
                contRighe += 1
                if rigaAttuale > 1:
                    return False

    for i in range(lunColonne):
        colonnaAttuale = 0
        for j in range(lunRighe):
            if mat[j][i] == 0:
                colonnaAttuale += 1
                contColonne += 1
                if colonnaAttuale > 1:
                    return False


    return contRighe == lunRighe and contColonne == lunColonne

main()