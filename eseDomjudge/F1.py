def main():
    N = int(input())
    M = int(input())
    L = creaIntervallo(N, M)
    trovato = checkNumeri(L)
    if trovato:
        print("SI", end="")
    else:
        print("NO", end="")


def controlloDivisori(n):
    somma = 0
    for i in range(2, n):
        if n % i == 0:
            somma += i
    return somma


def checkNumeri(L):
    mini = L[0]
    maxi = L[len(L)-1]
    count = 0
    while count < len(L):
        controllo = controlloDivisori(L[count])

        if mini <= controllo <= maxi:
            if L[count] == controlloDivisori(controllo):
                return True
        count += 1
    return False


def creaIntervallo(min, max):
    l = []
    for i in range(min, max + 1):
        l.append(i)
    return l


main()
