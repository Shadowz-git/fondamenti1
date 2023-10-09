a = []
indice = -1

pos = [0, 0]

righe = []
colonne = []


def main() -> None:
    global a
    k = int(input())
    for i in range(k):
        a.append(int(input()))

    n = int(input())
    m = int(input())
    mat = creaMatrice(n, m)
    spostati(mat, 0, 1)
    for riga in mat:
        for e in riga:
            print(e, end="")
        print()


def creaMatrice(r: int, c: int) -> list:
    m = []
    for i in range(r):
        m.append([])
        for j in range(c):
            m[i].append("a")

    return m


def getValori() -> int:
    global a
    global indice
    if indice == len(a) - 1:
        indice = 0
    else:
        indice += 1

    return a[indice]


def spostati(mat: list, start: int, step: int):
    global pos, righe, colonne

    if pos[0] >= len(mat) or pos[0] < 0:
        reset()
        return
    if pos[1] >= len(mat[0]) or pos[1] < 0:
        reset()
        return

    if step == 1:
        end = len(mat[0]) - 1
        while end in colonne:
            end -= 1
            if end < start:
                reset()
                return
        for i in range(start, end):
            if mat[pos[0]][i] == "a":
                mat[pos[0]][i] = getValori()

        righe.append(pos[0])
        pos[1] = end
        spostati(mat, pos[0], 2)
    elif step == 2:
        end = len(mat) - 1
        while end in righe:
            end -= 1
            if end < start:
                if pos[1] in colonne:
                    reset()
                    return
                else:
                    end = start
                    break
        if pos[0] == pos[1] or start == end:
            end += 1
        for i in range(start, end):
            if mat[i][pos[1]] == "a":
                mat[i][pos[1]] = getValori()
        colonne.append(pos[1])
        pos[0] = end
        spostati(mat, pos[1], 3)
    elif step == 3:
        end = 0
        while end in colonne:
            end += 1
            if end > start:
                reset()
                return
        for i in range(start, end, -1):
            if mat[pos[0]][1] == "a":
                mat[pos[0]][i] = getValori()

        righe.append(pos[0])
        pos[1] = end
        spostati(mat, pos[0], 4)
    elif step == 4:
        end = 0
        while end in righe:
            end += 1
            if end > start:
                if pos[1] in colonne:
                    reset()
                    return
                else:
                    end = start
                    break
        if pos[0] == pos[1] or start == end:
            end -= 1
        for i in range(start, end - 1, -1):
            if mat[i][pos[1]] == "a":
                mat[i][pos[1]] = getValori()
        colonne.append(pos[1])

        pos[0] = end
        spostati(mat, pos[1], 1)


def reset() -> None:
    global pos, righe, colonne, indice, a
    indice = -1
    pos = [0, 0]
    colonne = []
    righe = []
    a = []


main()
