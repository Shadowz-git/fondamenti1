s = input()
minuscole = "abcdefghijklmnopqrstwxyz"
maiuscole = "ABCDEFGHIJKLMNOPQRSTWXYZ"
trovato = False
precedente = ''

while not s.endswith('*'):
    s += input()

if len(s) > 1:
    for i in range(1, len(s[:-1])):
        if s[i-1] in maiuscole and s[i] in maiuscole:
            trovato = True
        elif (s[i-1] in minuscole and s[i] in minuscole) and s[i-1] == s[i]:
            trovato = True

if trovato:
    print("SI", end='')
else:
    print("NO", end='')