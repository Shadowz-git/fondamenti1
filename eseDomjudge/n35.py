valore = int(input())
somma = 0

while valore != 0:
    misura = input()
    if misura == "h":
        somma += valore*60*60
    elif misura == "m":
        somma += valore*60
    elif misura == "s":
        somma += valore

    valore = int(input())

print(somma, end="")