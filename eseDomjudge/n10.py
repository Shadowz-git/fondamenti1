n = input()
numeroP = int(n)
numeroR = ""

for i in range(len(n)-1, -1, -1):
    numeroR += n[i]

numeroR = int(numeroR)

print(numeroP - numeroR, end="")
