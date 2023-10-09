def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(int(input()))
    R = ricorsiva(L, [], 0)
    for i in R:
        print(i, end='')


def ricorsiva(ori, new, x):
    if x >= len(ori):
        return new
    new.insert(0, ori[x])
    return ricorsiva(ori, new, x+1)


main()