def main() -> None:
    n = int(input())
    m = int(input())
    s = []
    for i in range(n):
        s.append(int(input()))

    s1 = []
    for i in range(m):
        s1.append(int(input()))

    if checkSottoinsieme(s, s1) and checkSumfree(s1):
        print('OK', end='')
    else:
        print('NO', end='')


def checkSottoinsieme(lista1: list, lista2: list) -> bool:
    for i in range(len(lista2)):
        if lista2.count(lista2[i]) > 1:
            return False
        if lista2[i] not in lista1:
            return False

    return True


def checkSumfree(lista: list) -> bool:
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if (lista[i] + lista[j]) in lista:
                return False

    return True


main()
