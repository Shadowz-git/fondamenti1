minuscole = "abcdefghijklmnopqrstwxyz"
maiuscole = "ABCDEFGHIJKLMNOPQRSTWXYZ"

s = input()
ok = False

while not s.endswith('*'):
    s += input()

if len(s) > 2:
    for i in range(1, len(s[:-1])):
        if (s[i-1] == s[i] and s[i-1]) and ((s[i-1] in minuscole and s[i] in minuscole) or (s[i-1] in maiuscole and s[i] in maiuscole)):
            ok = True

if ok:
    print("SI", end='')
else:
    print("NO", end='')