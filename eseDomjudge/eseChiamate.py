chiamate = int(input())
costo = 0.0

if chiamate > 190:
    costo = costo + ((chiamate - 190) * 0.05)
    chiamate -= (chiamate - 190)  # chiamate = chiamate - (chiamate - 190)

if 140 < chiamate <= 190:
    costo = costo + ((chiamate - 140) * 0.07)
    chiamate -= (chiamate - 140)  # chiamate = chiamate - (chiamate - 140)

if 80 < chiamate <= 140:
    costo = costo + ((chiamate - 80) * 0.1)
    chiamate -= (chiamate - 80)  # chiamate = chiamate - (chiamate - 80)

if chiamate <= 80:
    costo = costo + 5
    print(round(costo, 3), end="")
