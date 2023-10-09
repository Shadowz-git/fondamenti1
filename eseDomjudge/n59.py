def main() -> None:
    n = int(input())
    mat = creaMatrice(n, n)
    maggiore = checkSomma(mat)
    if maggiore:
        print("OK", end='')
    else:
        print("NO", end='')


def creaMatrice(r: int, c: int) -> list:
    m = []
    for i in range(r):
        m.append([])
        for j in range(c):
            m[i].append(int(input()))

    return m


def checkSomma(lista: list) -> bool:
    meta = len(lista)//2
    sommaCroce = 0
    somma = 0
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i == meta:
                sommaCroce += lista[i][j]

            elif j == meta:
                sommaCroce += lista[i][j]

            else:
                somma += lista[i][j]

    return sommaCroce > somma


main()
