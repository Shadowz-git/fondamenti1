def main():
    somma = 0
    count = 0
    n = int(input())
    L = []
    while n != -50:
        somma += n
        L.append(n)
        count += 1
        n = int(input())

    if count == 0:
        print("VUOTA", end='')
    else:
        media = somma//count
        piccolo = 1000
        for x in L:
            if x >= media and x < piccolo:
                piccolo = x
        print(piccolo, end="")


main()
