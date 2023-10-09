import random

random.seed(0)

punteggioPC = 0
punteggioUS = 0
vincitore = 0

while punteggioUS != 3 and punteggioPC != 3:
    pc = random.randint(1, 3)
    giocata = int(input("Inserisci la giocata del primo giocatore (1: sasso, 2: carta, 3: forbice):"))
    while giocata > 3 or giocata < 1:
        giocata = int(input("Inserisci la giocata del primo giocatore (1: sasso, 2: carta, 3: forbice):"))
    if giocata == 1:
        giocata = "sasso"
    elif giocata == 2:
        giocata = "carta"
    elif giocata == 3:
        giocata = "forbice"
    print("hai giocato " + giocata)
    if pc == 1:
        giocataPC = "sasso"
        if giocata == "carta":
            vincitore = 1
        elif giocata == "forbice":
            vincitore = 2
    elif pc == 2:
        giocataPC = "carta"
        if giocata == "forbice":
            vincitore = 1
        elif giocata == "sasso":
            vincitore = 2
    elif pc == 3:
        giocataPC = "forbice"
        if giocata == "sasso":
            vincitore = 1
        elif giocata == "carta":
            vincitore = 2
    print("il PC ha giocato " + giocataPC)
    if giocataPC == giocata:
        print("Pari:")
    elif vincitore == 1:
        vincitore = 0
        punteggioUS += 1
        print("Vinci tu:")
    elif vincitore == 2:
        vincitore = 0
        punteggioPC += 1
        print("Vince il PC:")
    print(str(punteggioUS) + "-" + str(punteggioPC))

    if punteggioUS == 3:
        print("Hai vinto la sfida!")
    elif punteggioPC == 3:
        print("Il PC ha vinto la sfida!")