def main():
    stringa = input()
    controllo = checkStringa(stringa)
    print(controllo, end='')

def checkStringa(s):
    L = [0]*26
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for x in s:
        if x in alfabeto:
            for i in range(len(alfabeto)):
                if x == alfabeto[i]:
                    L[i] += 1
                    break
    for x in L:
        if x == 0:
            return "NO"
    return "SI"

main()
