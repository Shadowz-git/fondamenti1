def main():
    n = int(input())
    L = []
    for i in range(n):
        L.append(int(input()))

    print(palindroma(L, 0), end='')


def palindroma(l, x):
    if len(l) % 2 != 0:
        return "NO"
    if x >= len(l)//2:
        return "SI"
    if l[x] == l[(len(l)//2)+x]:
        return palindroma(l, x+1)
    else:
        return "NO"


main()
