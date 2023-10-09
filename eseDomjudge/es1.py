def main() -> None:
    n = int(input())
    m = int(input())
    numero = numeroDivisori(n)
    if controlloDivisori(n, numero):
        print('OK1', end='')
    else:
        print('NO1', end='')

    if controlloNumeri(n, m):
        print('OK2', end='')
    else:
        print('NO2', end='')


def numeroDivisori(numero: int) -> int:
    totale = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            totale += 1

    return totale


def controlloNumeri(base: int, trovato) -> bool:
    l = []

    for i in range(1, base):
        l.append(numeroDivisori(i))

    if l.count(trovato) > 0:
        return True

    return False


def controlloDivisori(numero: int, controllo: int) -> bool:
    if numero < 0:
        return False

    for i in range(0, numero):
        if numeroDivisori(i) >= controllo:
            return False
    return True


main()
