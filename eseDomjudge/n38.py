num = []
somma = 0
count = 0
media = 0
for i in range(100):
    numero = int(input())
    if numero < -50 or numero > 50:
        num.append(numero)
    else:
        somma += numero
        count += 1

if len(num) > 0:
    for i in num:
        print(i, end="")
    print()
else:
    print("VUOTO1")

if count > 0:
    media = round(somma / count, 6)
    print(media, end="")
else:
    print("VUOTO2", end="")
