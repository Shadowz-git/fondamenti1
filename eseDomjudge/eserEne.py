seme_briscola = int(input())
seme_carta_primo_giocatore = int(input())
carta_giocata_primo_giocatore = int(input())
seme_carta_secondo_giocatore = int(input())
carta_giocata_secondo_giocatore = int(input())
a = seme_briscola
b = seme_carta_primo_giocatore
c = carta_giocata_primo_giocatore
d = seme_carta_secondo_giocatore
e = carta_giocata_secondo_giocatore
if c == 1:
    c = 11
elif c == 3:
    c = 10.5
if e == 1:
    e = 11
elif e == 3:
    e = 10.5
if a >= 1 and a <= 4:
    if b == a and d == a:
        if c > e:
            print("VINCE GIOCATORE 1", end="")
        else:
            print("VINCE GIOCATORE 2", end="")
    elif b == a and d != a:
        print("VINCE GIOCATORE 1", end="")
    elif b != a and d == a:
        print("VINCE GIOCATORE 2", end="")
    elif b != a and d != a:
        if b != d:
            print("VINCE GIOCATORE 1", end="")

