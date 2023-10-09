def main():
    X = int(input())
    N = int(input())
    L = []
    for i in range(N):
        L.append(int(input()))

    numero = ricorsiva(L, X)
    print(numero, end="")


def ricorsiva(L, x):
    count = 0
    for i in range(len(L)):
        if L[i] == x:
            L[i] = 0
            count += 1
    if count == 0:
        return 0
    return count + ricorsiva(L, count)


main()
