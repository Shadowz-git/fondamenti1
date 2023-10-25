n1 = None
n2 = None
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main() -> None:
    global n1, n2
    n1 = int(input())
    n2 = int(input())
    l = []
    s = input()
    while s != ".":
        l.append(s)
        s = input()

    if len(l) > 0:
        print(cifrare(l), end='')


def cifrare(lista: list) -> str:
    l = ""
    for i in range(len(lista)):
        if lista[i] in alfabeto:
            if i % 2 == 0:
                l += cifrareChar(lista[i], "d")
            else:
                l += cifrareChar(lista[i], "s")

    return l


def cifrareChar(char: str, pos: str) -> str:
    posChar = alfabeto.index(char)
    if pos == "s":
        return alfabeto[posChar - n2]
    elif pos == "d":
        if posChar + n1 > 25:
            return alfabeto[posChar + n1 - 26]
        return alfabeto[posChar + n1]


main()
