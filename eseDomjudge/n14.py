s = input()
somma = 0

while not s.endswith('00'):
    s += input()

for i in range(len(s[:-2])):
    if (int(s[i]) == 0 and int(s[i+1]) != 0):
        print(somma)
        somma = 0
    elif (int(s[i]) != 0 and int(s[i+1]) == 0 and int(s[i+2]) == 0):
        if somma != 0:
            print(somma)
        else:
            print(int(s[i]))
    elif int(s[i]) != 0:
        somma += int(s[i])
