debolezze = [[], []]


def main() -> None:
    n = int(input())
    intervallo = []
    for i in range(1, n + 1):
        intervallo.append(i)
    print(maxDebolezze(intervallo), end='')


def numeroDivisori(numero: int) -> int:
    somma = 1
    for i in range(1, numero//2 + 1):
        if numero % i == 0:
            somma += 1
    return somma


def calcDebolezza(numero: int) -> int:
    divisore = numeroDivisori(numero)
    deb = 0
    for i in range(1, numero):
        if numeroDivisori(i) > divisore:
            deb += 1
    return deb


def checkDebolezza(numero: int) -> int:
    global debolezze
    if debolezze[0].count(numero) == 0:
        debolezze[0].append(numero)
        debolezza = calcDebolezza(numero)
        debolezze[1].append(debolezza)
    else:
        indice = debolezze[0].index(numero)
        debolezza = debolezze[1][indice]

    return debolezza


def maxDebolezze(numeri: list) -> int:
    massimo = 0
    for i in numeri:
        debolezza = checkDebolezza(i)
        if debolezza > massimo:
            massimo = debolezza

    return massimo


main()
