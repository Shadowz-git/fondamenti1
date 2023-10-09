PIANO = []
# Crea il piano
for i in range(20):
    PIANO.append([])
    for j in range(20):
        PIANO[i].append(0)


def visualizzaPavimento(pavimento, dim):
    for i in range(dim):
        for j in range(dim):
            if pavimento[i][j] == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


# Posizione della tartaruga
tartaruga = [0, 0]


def sposta(pos):
    """
    Se la posizione è 'E' va a destra
    Se la posizione è 'O', va a sinistra
    Se la posizione è 'N', va sopra
    Se la posizione è 'S', va sotto

    :param pos:
    :return:
    """
    s = int(input("passi?"))
    print()
    # -->
    if pos == "E":
        temp = tartaruga[1]
        if tartaruga[1] + s > 19:
            tartaruga[1] = 19
        else:
            tartaruga[1] = tartaruga[1] + s
        casellaScritta(PIANO, temp, tartaruga[1], "c")
    # < --
    elif pos == "O":
        temp = tartaruga[1]
        if tartaruga[1] - s < 0:
            tartaruga[1] = 0
        else:
            tartaruga[1] = tartaruga[1] - s
        casellaScritta(PIANO, temp, tartaruga[1], "c")
    # Giù
    elif pos == "S":
        temp = tartaruga[0]
        if tartaruga[0] + s > 19:
            tartaruga[0] = 19
        else:
            tartaruga[0] = tartaruga[0] + s
        casellaScritta(PIANO, temp, tartaruga[0], "r")
    # Su
    elif pos == "N":
        temp = tartaruga[0]
        if tartaruga[0] - s < 0:
            tartaruga[0] = 0
        else:
            tartaruga[0] = tartaruga[0] - s
        casellaScritta(PIANO, temp, tartaruga[0], "r")


# Variabile per indicare se ha cominciato a scrivere
startato = False


def casellaScritta(lista, from_where, to_where, tipo):
    """Scrive le caselle, se la penna è abbassata
        Lista: è il piano
        from_where: posizione da dove inizia
        to_where: posizione di arrivo
        tipo: se 'c' vuol dire colonna, se 'r' è riga
    """
    global startato
    if penna:
        if tipo == "c":
            # Se da dove inizia è maggiore rispetto al punto di arrivo, deve scalare
            if from_where > to_where:
                if not startato:
                    from_where -= 1
                for i in range(from_where, to_where - 1, -1):
                    lista[tartaruga[0]][i] = 1
            else:
                if not startato:
                    from_where += 1
                for i in range(from_where, to_where + 1):
                    lista[tartaruga[0]][i] = 1
        elif tipo == "r":
            # Se da dove inizia è maggiore rispetto al punto di arrivo, deve scalare
            if from_where > to_where:
                if not startato:
                    from_where -= 1
                for i in range(from_where, to_where - 1, -1):
                    lista[i][tartaruga[1]] = 1
            else:
                if not startato:
                    from_where += 1
                for i in range(from_where, to_where + 1):
                    lista[i][tartaruga[1]] = 1


comandi = []
cont = 0
terminato = False
numeri = "12345678"

while cont < 100 and not terminato:
    n = input()
    if n == "9":
        terminato = True
    elif n in numeri:
        comandi.append(int(n))
    cont += 1

# abbassata True, alzata False
penna = True


def main():
    global penna
    for x in comandi:
        if x == 1:
            penna = False
        elif x == 2:
            penna = True
        elif x == 3:
            sposta("E")
        elif x == 4:
            sposta("O")
        elif x == 5:
            sposta("S")
        elif x == 6:
            sposta("N")
        elif x == 7:
            visualizzaPavimento(PIANO, 20)


main()
