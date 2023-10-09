L = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

count = 0
while count != 10:
    richiesta = int(input("Digitare 1 per fumatori o 2 per non fumatori:"))
    trovato = False
    if richiesta == 1:
        for i in range(0,5):
            if not trovato and L[i] == 0:
                trovato = True
                L[i] = 1
                count += 1
                print("Reparto fumatori, posto", i+1)
        if not trovato:
            richiesta2 = input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?")
            while richiesta2 != "S" and richiesta2 != "N":
                richiesta2 = input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?")
            if richiesta2 == "N":
                print("Il prossimo volo parte tra 3 ore")
            elif richiesta2 == "S":
                for i in range(5, 10):
                    if not trovato and L[i] == 0:
                        trovato = True
                        L[i] = 1
                        count +=1

                        print("Reparto NON fumatori, posto", i +1)
    elif richiesta == 2:
        for i in range(5,10):
            if not trovato and L[i] == 0:
                trovato = True
                L[i] = 1
                count += 1
                print("Reparto NON fumatori, posto", i + 1)
        if not trovato:
            richiesta2 = input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?")
            while richiesta2 != "S" and richiesta2 != "N":
                richiesta2 = input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?")
            if richiesta2 == "N":
                print("Il prossimo volo parte tra 3 ore")
            elif richiesta2 == "S":
                for i in range(0, 5):
                    if not trovato and L[i] == 0:
                        trovato = True
                        L[i] = 1
                        count +=1
                        print("Reparto fumatori, posto", i + 1)
