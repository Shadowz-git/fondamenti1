lato = int(input())
lato2 = int(input())
lato3 = int(input())

if (lato + lato2 < lato3) or (lato + lato3 < lato2) or (lato2 + lato3 < lato):
    print("NO", end="")
elif (lato == lato2 and lato != lato3) or (lato == lato3 and lato2 != lato) or (lato2 == lato3 and lato2 != lato):
    print("TRIANGOLO ISOSCELE", end="")
elif lato == lato2 and lato2 == lato3:
    print("TRIANGOLO EQUILATERO", end="")
else:
    print("TRIANGOLO SCALENO", end="")