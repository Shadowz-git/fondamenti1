M = int(input())
N = int(input())
primo = True
secondo = True


if M % 2 != 0:
    for i in range(3, M, 2):
        if M % i == 0:
            primo = False
else:
    if M != 2:
        primo = False


if primo and N % 2 != 0:
    for i in range(3, N, 2):
        if N % i == 0:
            secondo = False
else:
    if N != 2:
        secondo = False

if primo and secondo:
    gemelli = abs(M - N)

    if gemelli == 2:
        print("gemelli", end="")
    else:
        print("non gemelli", end="")
else:
    print("non entrambi primi", end="")
