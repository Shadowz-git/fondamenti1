n = input()
zero = False

if int(n) != 0:
    for i in n:
        num = int(i)
        if num == 0:
            zero = True
    if zero:
        print("NO", end="")
    else:
        print("SI", end="")
else:
    print("NO", end="")

