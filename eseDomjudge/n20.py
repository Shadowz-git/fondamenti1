s = input()
lettere = "abcdefghijklmnopqrstwxyzABCDEFGHIJKLMNOPQRSTWXYZ"
soloLettere = True

while s != '.':
    if s not in lettere:
        soloLettere = False
    s = input()

if soloLettere:
    print("SI", end='')
else:
    print("NO", end='')
