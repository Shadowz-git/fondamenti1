def main():
    A = int(input())
    B = int(input())
    MCD = MassimoComunDivisore(A, B)
    print(MCD, end='')


def MassimoComunDivisore(a, b):
    if a == 0 or b == 0:
        return 0

    r = a % b
    if r == 0:
        return b
    return MassimoComunDivisore(b, r)


main()
