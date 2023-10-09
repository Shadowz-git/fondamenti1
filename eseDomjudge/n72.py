
def main():
    esatta = input()
    risultati = []
    risposteDate(esatta, risultati)
    output(risultati)


def output(L):
    for i in L:
        print(i[0], i[1])


def risposteDate(esatta, L):
    for i in range(90):
        matricola = input()
        risposta = input()
        risultato = controlloRisultato(risposta, esatta)
        L.append([matricola, risultato])


def controlloRisultato(stringa, esatta):
    somma = 0
    for i in range(len(stringa)):
        if stringa[i] == esatta[i]:
            somma += 2
        elif stringa[i] == "X":
            continue
        elif stringa[i] != esatta[i]:
            somma -= 1

    return somma


main()