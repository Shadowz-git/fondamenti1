def main():
    n = int(input())
    r = ricorsivo(n)
    print(r, end='')


def ricorsivo(n):
    if n == 0:
        return 2
    return 3 * (n+1) * ricorsivo(n-1)

main()
