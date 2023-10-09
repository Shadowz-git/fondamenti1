N = input()
Nmax = 0
Nmin = 0
num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
stringa = ""

if N != "0":
    for x in N:
        numero = int(x)
        num[numero] += 1

    for i in range(9, 0, -1):
        if num[i] > 0:
            stringa += str(i) * num[i]

    Nmin = int(stringa[::-1])
    if num[0] > 0:
        for i in range(num[0]):
            stringa += "0"

    Nmax = int(stringa)
    print(Nmax-Nmin, end="")
else:
    print(0, end="")
