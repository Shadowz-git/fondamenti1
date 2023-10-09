stringa = ""
s = input()
vocali = "aeiou"

for i in range(len(s)):
    if s[i] in vocali:
        stringa += s[i] + "f" + s[i]
    else:
        stringa+= s[i]

lenStringa = len(stringa)//2

print(stringa[lenStringa:len(stringa)+1] + stringa[0:lenStringa], end="")

