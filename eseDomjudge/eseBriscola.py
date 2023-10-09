semeBriscola = int(input())
semeGiocatore1 = int(input())
cartaGiocatore1 = int(input())
semeGiocatore2 = int(input())
cartaGiocatore2 = int(input())

if cartaGiocatore1 == 1:
    cartaGiocatore1 = 12
elif cartaGiocatore1 == 3:
    cartaGiocatore1 = 11

if cartaGiocatore2 == 1:
    cartaGiocatore2 = 12
elif cartaGiocatore2 == 3:
    cartaGiocatore2 = 11

if (semeBriscola == semeGiocatore1 and semeGiocatore2 != semeBriscola) or (semeGiocatore1 != semeGiocatore2 and semeGiocatore2 != semeBriscola):
    print("VINCE GIOCATORE 1", end="")
elif semeBriscola != semeGiocatore1 and semeGiocatore2 == semeBriscola:
    print("VINCE GIOCATORE 2", end="")
elif semeGiocatore2 == semeGiocatore1:
    if cartaGiocatore1 > cartaGiocatore2:
        print("VINCE GICATORE 1", end="")
    else:
        print("VINCE GIOCATORE 2", end="")
