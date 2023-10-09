def main() -> None:
    n = int(input())
    print(arrontodamento(n), end='')


def arrontodamento(numero: int) -> int:
    tempNum = numero
    count = 1
    while tempNum != 0:
        div = 10**count
        num = numero % div
        if tempNum % 10 >= 5 and tempNum // 10 != 0:
            numero = numero - num + 10**count
            tempNum = numero // 10**count
        elif tempNum % 10 < 5 and tempNum // 10 != 0:
            numero -= num
            tempNum = numero // 10**count

        if tempNum // 10 == 0:
            tempNum //= 10

        count += 1
    return numero


main()
