def main():
    N = input()
    numeroCom = sostituisci(N)
    print(numeroCom, len(numeroCom), end='')


def sostituisci(num):
    stringa = ''
    cont = 1
    for i in range(0, len(num)-1):
        if num[i] == num[i+1]:
            cont += 1
        elif num[i] != num[i+1]:
            stringa += str(cont) + num[i]
            cont = 1
    if len(num) > 1:
        if num[-2] == num[-1]:
            stringa += str(cont) + num[-1]
        elif num[-2] != num[-1]:
            stringa += '1' + num[-1]
    elif len(num) <= 1:
        if len(num) == 1:
            return '1' + num
        else:
            return '0'

    return stringa

main()
