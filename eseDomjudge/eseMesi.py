mese = int(input())

if mese == 3 or mese == 6 or mese == 9 or mese == 12:
    giorno = int(input())
    """Questo è uno shorthand, sarebbe:
    if 1 <= giorno <= 20:
        mese = mese - 1
    else:
        mese = mese
        
    Si, si possono fare questi if mono riga per queste cose
    Anche se è meglio scrivere un if come ^^
    """
    mese = mese - 1 if (1 <= giorno <= 20) else mese

if 12 == mese or mese <= 2:
    print("INVERNO", end="")
elif 3 <= mese <= 5:
    print("PRIMAVERA", end="")
elif 6 <= mese <= 8:
    print("ESTATE", end="")
elif 9 <= mese <= 11:
    print("AUTUNNO", end="")
else:
    print("MESE NON VALIDO", end="")
