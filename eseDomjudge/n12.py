n = int(input())

if n % 2 != 0:
    for i in range(3, n, 2):
        if n % i == 0:
            print("NO", end="")
            break
    else:
        print("SI", end="")
else:
    print("NO", end="")