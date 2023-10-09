L = []
L2 = []
s = input()
Trovato = False

while s != ".":
    L.append(s)
    s = input()

s = input()
while s != ".":
    L2.append(s)
    s = input()

for i in L:
    for j in L2:
        if i == j and not Trovato:
            Trovato = True
            print(i, end="")

if not Trovato:
    print("DISGIUNTE", end="")