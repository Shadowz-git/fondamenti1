def main() -> None:
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    lista = creaLista()
    output = controlloOutput(lista, alfabeto)
    print(output, end='')


def creaLista() -> list:
    n = input()
    lista = []

    while n != '*':
        lista.append(n)
        n = input()

    return lista


def controlloOutput(lista: list, alfabeto: str) -> int:
    massimo = 0
    count = 1
    massimoCount = 0
    lung = len(lista)
    for i in range(1, lung):
        if (alfabeto.index(lista[i])) <= alfabeto.index(lista[i - 1]):
            count += 1
            output = alfabeto.index(lista[i-count+1]) - alfabeto.index(lista[i]) - 1

            if count >= massimoCount:
                massimoCount = count
                if output > massimo:
                    massimo = output
        else:
            count = 1
    return massimo


main()
