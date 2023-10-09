s = input()
count = 0
ok = False

while not s.endswith('*'):
    s += input()

if len(s) > 2:
    for i in range(1, len(s[:-1])):
        if s[i-1] == s[i] and s[i-1]:
            ok = True

if ok:
    print("SI", end='')
else:
    print("NO", end='')