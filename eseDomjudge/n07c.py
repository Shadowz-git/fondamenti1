n = int(input())
elettore1 = 0
elettore2 = 0
elettore3 = 0
vincitore = 0

while n != 0:
    if n == 1:
        elettore1 += 1
    elif n == 2:
        elettore2 += 1
    else:
        elettore3 += 1
    n = int(input())

votiTotali = elettore1 + elettore2 + elettore3

if votiTotali > 0:
    voti1 = round(elettore1/votiTotali*100, 1)
    voti2 = round(elettore2/votiTotali*100, 1)
    voti3 = round(elettore3/votiTotali*100, 1)

    if voti1 > 50:
        vincitore = 1
    elif voti2 > 50:
        vincitore = 2
    elif voti3 > 50:
        vincitore = 3

    print("1", elettore1, voti1)
    print("2", elettore2, voti2)
    print("3", elettore3, voti3)
    if vincitore == 0:
        print("BALLOTTAGGIO", end="")
    else:
        print("VINCE", vincitore, end="")

else:
    print("BALLOTTAGGIO", end="")

