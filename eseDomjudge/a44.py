def main():
    s = input()
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2:]
    somma1 = 0
    somma2 = 0
    for i in s1:
        somma1 += int(i)

    for i in s2:
        somma2 += int(i)

    if somma1 == somma2:
        print("FORTUNATO", end='')
    else:
        print("SFORTUNATO", end='')


main()
