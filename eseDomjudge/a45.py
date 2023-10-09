def main():
    M = input()
    numeri = "1234567890"
    lettere = "abcdefghijklmnopqrstuvwxyz_"
    check = True
    if M[0] in numeri:
        check = False

    for i in M:
        if i.lower() not in lettere and i not in numeri or i == " ":
            check = False

    if check:
        print("SI", end='')
    else:
        print("NO", end='')


main()
