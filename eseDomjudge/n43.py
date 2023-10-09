stringa = input()
aperta = 0
chiusa = 0
prima = True
seconda = True

for i in range(len(stringa)):
    if stringa[i] == "(":
        aperta += 1
        if aperta < chiusa:
            prima = False
    elif stringa[i] == ")":
        chiusa += 1

if "()" in stringa:
    seconda = False

if aperta != chiusa:
    prima = False

if prima:
    print("ok1")
else:
    print("no1")

if seconda:
    print('ok2')
else:
    print("no2")