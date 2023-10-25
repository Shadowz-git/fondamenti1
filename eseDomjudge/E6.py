def main() -> None:
    numeroBrani = int(input())
    annoControllo = int(input())
    lista = creaLista(numeroBrani)
    annoMigliore = checkAnno(lista)
    riproduzioni = checkRiproduzioni(lista, annoControllo)
    print(str(annoMigliore) + " " + riproduzioni, end='')


def creaLista(num: int):
    l = []
    for i in range(num):
        l.append([int(input()), int(input())])

    return l


def checkAnno(lista: list):
    count = 0
    index = 0
    temp = 0
    massimo = 0

    for a in lista:
        anno = a[1]
        for i in range(0, len(lista)):
            if lista[i][1] == anno:
                count += 1
        if count > massimo:
            massimo = count
            index = anno
        count = 0

    return index


def checkRiproduzioni(lista: list, anno: int):

    for i in range(len(lista)):
        if lista[i][1] == anno and lista[i][0] != 0:
            return 'NO'

    return 'SI'


main()
