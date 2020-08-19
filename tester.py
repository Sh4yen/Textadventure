def entscheidung(a,b,c,d,e,f):
    print(a)
    if b == "-":
        pass
    else: 
        print("1. ", b)
    if c == "-":
        pass
    else:
        print("2. ", c)
    if d == "-":
        pass
    else:
        print("3. ", d)
    if e == "-":
        pass
    else:
        print("4. ", e)
    if f == "-":
        pass
    else:
        print("5. ", f)
    
    auswahl = str(input())
    if auswahl == "1" or auswahl == "b":
        return 1
    elif auswahl == "2" or auswahl == "c":
        return 2
    elif auswahl == "3" or auswahl == "d":
        return 3
    elif auswahl == "4" or auswahl == "e":
        return 4
    elif auswahl == "5" or auswahl == "f":
        return 5
    else:
        for i in range(len(inventarliste)):
            if auswahl == inventarliste[i]:
                print("Du verwendest ", inventarliste[i])
            else:
                pass
ergebniss = entscheidung("Was kannst du", "Nichts", "Viel", "-", "Fußball", "Koks und Nutten")
print(ergebniss)