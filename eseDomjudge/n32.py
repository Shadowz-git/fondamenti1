n = int(input())
precedente = 0
crescente = True
ok = True
count = 0

while n != 0:
    if count > 0 and crescente:
        if n <= precedente:
            crescente = False
            if count == 1:
                ok = False
    if count > 0 and not crescente:
        if n >= precedente:
            ok = False

    count += 1
    precedente = n
    n = int(input())

if ok and count > 2 and not crescente:
    print("SI", end='')
else:
    print("NO", end="")
