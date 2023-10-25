def main() -> None:
    numeri = creaLista()
    rapporti = controlloIncrementi(numeri)
    print(rapporti, end='')


def creaLista() -> list:
    n = input()
    lista = []

    while n != '*':
        lista. append(int(n))
        n = input()

    return lista


def controlloIncrementi(numbers: list):
    count = 1
    rapporti = 0
    for i in range(len(numbers)-1):
        if (numbers[i] + 1) == numbers[i+1]:
            count += 1
            if i == len(numbers) - 2:
                rapporti += 1
        elif (numbers[i] + 1) != numbers[i+1]:
            if count >= 2:
                rapporti += 1
            count = 1

    return rapporti


main()

