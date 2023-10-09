def main():
    n = int(input())
    romboidale = isRombo(n)
    print(romboidale, end='')


def isRombo(n):
    somma = 2
    prec = 1
    if n == 1:
        return 1

    for i in range(1, n):
        if i == n-1:
            somma += prec + 2
        else:
            somma += 2*(prec + 2)
        prec += 2

    return somma


main()
