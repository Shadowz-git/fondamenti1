N = int(input())
n = int(input())
count = 0
ok = False

while n != -1:
    if n <= N:
        count += 1
        if count == N:
            ok = True
    else:
        count = 0
    n = int(input())

if ok or N == 0:
    print("OK", end='')
else:
    print("NO", end="")