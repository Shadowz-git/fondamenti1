vocale = ""
vocali = "aeiou"
trovata = False
vabene = True

for i in range(100):
    s = input()
    if s in vocali and not trovata:
        vocale = s
        trovata = True
    elif s in vocali and trovata and s != vocale:
        vabene = False

if vabene:
    print("OK", end="")
else:
    print("ERRORE", end="")
