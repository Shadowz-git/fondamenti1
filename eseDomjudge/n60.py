def main() -> None:
    stringa = input()
    n = int(input())
    stringhe = []
    for i in range(n):
        stringhe.append(input())

    if str(presentiStringhe(stringhe, stringa)) == "True":
        print('OK', end='')
    else:
        print(presentiStringhe(stringhe, stringa), end='')


def presentiStringhe(lista: list, controllo: str):
    grande = 0
    piccola = 0

    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] + lista[j] == controllo:
                return True
            elif lista[j] + lista[i] == controllo:
                return True
        if lista[i] > lista[grande]:
            grande = i
        if lista[i] < lista[piccola]:
            piccola = i

    return lista[grande] + lista[piccola]


main()
