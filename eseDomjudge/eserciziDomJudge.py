###
#n1
print("Buon divertimento!", end="")

###
#n1b
print("********************")
print("*Buon divertimento!*")
print("********************", end="")

###
#n1c
print("    +    ")
print("  +   +  ")
print(" +     + ")
print("+-------+")
print("|       |")
print("|       |")
print("|       |")
print("+-------+", end="")

####
#n1d
saldoMese1 = 500
saldoMese2 = (saldoMese1 - 5) * 1.02
saldoMese3 = (saldoMese2 - 5) * 1.02
print("PRIMO MESE:", saldoMese1)
print("SECONDO MESE:", round(saldoMese2))
print("TERZO MESE:", round(saldoMese3), end="")

###
#n1e
saldo_iniziale = int(input()) #1000
canone_mensile = int(input())
interessi = int(input())
interessi = interessi/100 + 1 #1 -> 0.01 + 1 -> 1.01
mese2 = (saldo_iniziale-canone_mensile) * interessi #1008
mese3 = (mese2-canone_mensile) * interessi #1016
print("PRIMO MESE:", saldo_iniziale)
print("SECONDO MESE:", round(mese2))
print("TERZO MESE:", round(mese3), end="")

####
#n2
a = int(input()) #3
b = int(input()) #5
print("Somma:", a + b) #8
print("Differenza:", a - b) #2
print("Moltiplicazione:", a * b) #15
print("Quoziente:", a // b) #1
print("Resto:", a % b) #2

####
#n2b
base = int(input()) #3
altezza = int(input()) #4
print("AREA:", base * altezza) #12
print("PERIMETRO:", (base*2)+(altezza*2), end="")

####
#n2c
stringa1 = input()
stringa2 = input()
print(stringa1 + stringa2, end="") #OPPURE print(stringa1, stringa2, sep="", end="")

####
#n2d
import math # -> math.sqrt
#from math import sqrt  -> sqrt
#from math import * -> sqrt

numero = int(input())
radice = math.sqrt(numero)
print(round(radice, 2), end="")