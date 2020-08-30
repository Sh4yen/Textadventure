inventarliste = []

def inventaradd(a):             #funktion mit parameter
    inventarliste.append(a)     #Parameter kommt in die Inventarliste
    print("--- " + a + " Wurde zu deinem Inventar hinzugefügt")

inventaradd("Monatskarte")      #Argument Monatskarte wird als parameter der funktion inventaradd eigesetzt und kommt so in die liste


def entscheidung(Frage,Antwort1,Antwort2,Antwort3,Antwort4,Antwort5):  #funktion Entscheidung. Parameter a = Text/Frage. Parameter b,c,d,e,f = Antwortmöglichkeiten
    print(Frage)
    if  Antwort1 == "-":                #wenn für einen Parameter das Argument - (Bindestrich) gegeben wird, so wird dieser ignorirt
        pass
    else: 
        print("1. ", Antwort1)
    if Antwort2 == "-":
        pass
    else:
        print("2. ", Antwort2)
    if Antwort3 == "-":
        pass
    else:
        print("3. ", Antwort3)
    if Antwort4 == "-":
        pass
    else:
        print("4. ", Antwort4)
    if Antwort5 == "-":
        pass
    else:
        print("5. ", Antwort5)
    
    auswahl = str(input())
    if auswahl == "1":    #wenn 1 gewält wird gibt die funktion 1 aus u.s.w.
        return 1
    elif auswahl == "2":
        return 2
    elif auswahl == "3":
        return 3
    elif auswahl == "4":
        return 4
    elif auswahl == "5":
        return 5
    else:
        for i in range(len(inventarliste)): #eine Zahl i steht bei null und wiederholt die for funktion bis sie bei der länge der list angelangt, jedes mal wird sie um 1 addiert
            if auswahl == inventarliste[i]: #stimmt das eingegebene wor mit einem Listenelement überein so wird der print befehl ausgeführt und die funktion gibt den Namen des elements aus
                print("Du verwendest " + inventarliste[i])
                return inventarliste[i]
            else:
                return 0    #gibt die Funktion 6 aus wurde keine Valide eingabe gemacht

print("Hallo")

clock = 0
while clock == 0 :
    clock = entscheidung("Um an bord zu kommen benötigen sie leider eine Karte, haben sie eine? \n(Tipp: du kannst dinge aus deinem Inventar nutzen indem du ihren Namen schreibst.)", "Nein Leider nicht.", "Wo bin ich hier?", "-", "-", "-")
    if clock == "Monatskarte":
        print ("toll")
        clock = 1
    elif clock == 1 :
        print ("nicht so toll")
        clock = 0
    elif clock == 2 :
        print ("Einer von den Langsamen hu, hier nochmal:")
        clock = 0


    
    