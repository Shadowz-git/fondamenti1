parole = []

def main() -> None:
    global parole
    righe = int(input())
    colonne = int(input())
    mat = creaMatrice(righe, colonne, True)
    checkMat = creaMatrice(righe, colonne, False)
    # numParole = int(input())
    # for i in range(numParole):
    #     parole.append(input())


def creaMatrice(r: int, c: int, coninput: bool) -> list:
    m = []
    for i in range(r):
        m.append([])
        for j in range(c):
            if coninput:
                m[i].append(input())
            else:
                m[i].append(0)

    return m


def segnaCheck(lista: list, indice: int, start: int, end: int, tipo: str, obliqua = []) -> list:
    if tipo == "r":
        for i in range(start, end + 1):
            lista[indice][i] = 1
    elif tipo == "c":
        for i in range(start, end + 1):
            lista[i][indice] = 1
    elif tipo == "o":
        for i in obliqua:
            lista[i[0]][i[1]] = 1


def checkparola(mat: list, indice: int, start: int, tipo: str) -> str:
    parola = ""
    if tipo == "or":
        for i in range(start, len(mat[indice])):
            parola += mat[indice][i]
        if parola in parole:
            parole.remove(parola)
            segnaCheck(mat, indice, start, len(mat[indice]) - 1, "r")
    elif tipo == "ve":
        for i in range(start, len(mat)):
            parola += mat[i][indice]
        if parola in parole:
            parole.remove(parola)
            segnaCheck(mat, indice, start, len(mat) - 1, "c")


def leggiOrizzontale(mat: list, index: int):
    if index >= len(mat) or index < 0:
        return
    for i in range(len(mat[index])):
        checkparola(mat, index, i, "or")
    return leggiOrizzontale(mat, index + 1)


def leggiVerticale(mat:list, index: int):
    if index >= len(mat[0]) or index < 0:
        return
    for i in range(len(mat)):
        checkparola(mat, i, index, "ve")
    return leggiVerticale(mat, index + 1)


def leggiDiagonali(mat:list, index: int):
    max_col = len(mat[0])
    max_riga = len(mat)
    num_diagonali = max_riga + max_col - 1
    diagonali = []

    for x in range(num_diagonali):
        diagonali.append([], [])

    for i in range(max_riga):
        for j in range(max_col):
            locale = i - j


def schemaOrizzontale(mat: list, check: list) -> list:
    for i in range(len(mat)):
        parola = ""
        lista = []
        for j in range(len(mat[i])):
            parola += mat[i][j]
            if parola in parole:
                
