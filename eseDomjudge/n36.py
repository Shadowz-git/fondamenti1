L = []
for i in range(10):
    L.append(int(input()))

X = int(input())
divisibile = False
for a in L:
    if a % X == 0:
        divisibile = True

if divisibile:
    print("NO", end='')
else:
    print('OK', end='')

