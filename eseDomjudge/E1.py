L = []
s = input()
funzione = True
controlli = "_abcdefghijklmnopqrstuvwzxyzABCDEFGHIJKLMNOPQRSTWXYZ"
numeri = "1234567890"

while s != ":":
    L.append(s)
    s = input()


def checkNome(check):
    for x in check:
        if x not in controlli and x not in numeri:
            return False
    return True


def controlloVar():
    global funzione
    if (len(L) - 4) % 2 == 0:
        funzione = False
    else:
        for i in range(3, len(L)-1):
            if i % 2 != 0 and (not checkNome(L[i]) or L[i] == ","):
                funzione = False
            elif i % 2 == 0 and L[i] != ",":
                funzione = False


if len(L) >= 4:
    for i in range(3):
        if i == 0 and L[i] != "def":
            funzione = False
        elif i == 1:
            if L[i][0] in numeri or not checkNome(L[i]):
                funzione = False
        elif i == 2 and L[i] != "(":
            funzione = False
    if len(L) > 4:
        controlloVar()
    if L[len(L)-1] != ")":
        funzione = False
else:
    funzione = False

if funzione:
    print("SI", end='')
else:
    print("NO", end='')
