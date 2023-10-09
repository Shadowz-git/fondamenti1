def main() -> None:
    pesiQuesiti = []
    for i in range(8):
        pesiQuesiti.append(int(input()))
    studenti = [[], []]
    for i in range(70):
        studenti[0].append(input())
        studenti[1].append([])
        for j in range(8):
            studenti[1][i].append(int(input()))
    soglia = int(input())
    listaPassati, numPassati, migliore, peggiore = calcoloVoto(studenti, pesiQuesiti, soglia)
    for i in range(len(listaPassati)):
        print("A" + str(listaPassati[i][0]), listaPassati[i][1])
    print(numPassati, studenti[0][migliore], studenti[0][peggiore], end='')


def calcoloVoto(esami: list, voti: list, soglia: int) -> int:
    voto = 0
    minimo = 1000
    indMinimo = 0
    massimo = 0
    indMassimo = 0
    listaPassati = []
    for i in range(len(esami[0])):
        for j in range(len(esami[1][i])):
            voto += esami[1][i][j] * voti[j]

        if voto >= soglia:
            listaPassati.append([i, voto])
            if voto > massimo:
                indMassimo = i
                massimo = voto
            if voto < minimo:
                indMinimo = i
                minimo = voto
        voto = 0

    return listaPassati, len(listaPassati), indMassimo, indMinimo


main()
