#Bibiloteken importieren
from tkinter import * 

#Entscheidungen
#Inventar
inventarliste = []


#gegenstand zuum Inventar hinzufügen
def inventaradd(a):           #funktion mit parameter
    inventarliste.append(a) #Parameter kommt in die Inventarliste

inventaradd("Monatskarte")     #Argument Monatskarte wird als parameter der funktion inventar+ eigesetzt und kommt so in die liste


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


ergebniss = 1
while ergebniss == 1 :
    ergebnissb = entscheidung("Hallo, um an bord zu kommen benötigen sie leider eine Karte haben sie eine? \n(Tipp: du kannst dinge aus deinem Inventar nutzen indem du ihren Namen schreibst.", "Nein Leider nicht.", "Wo bin ich hier?", "-", "-", "-")
    
    if ergebnissb == "Monatskarte":
        print("Toll")
        ergebniss = 0
        
   
    #Warum steht hier ergebnis = entscheidung 
    #wenn ich nicht das richtige eingebe komme ich trozdem weiter??!
    #die funktion muss loopen wenn eine ungültige antwort gegeben wird.
 
        
    






#spieler ruft inventar auf
def inventarrecall():
    for i in range (0, len(inventarliste), 1):  # loop mit variable i fängt bei 0 an zu zählen in 1er schritten bis zu länge der Liste definiert durch len(inventarliste)
        print(inventarliste[i])                 # i gibt die Listennummer an z.B. ist 0 gerade Monatskarte und der rest nicht definiert



#Spiel Start----------------------------------------------------------------------------------------------------------------------------------------------------


#Versuch Inventarliste
window = Tk()
Label(window, text="Inventar", font="none 30 bold") .grid(row=0, column=0, sticky=W)
for i in range(len(inventarliste)):
    Label(window, text=inventarliste[i], font="none 10 bold") .grid(row=i+1, column=0, sticky=W)



#Namenswahl
name = input("Was ist dein Name: ")
spiel = 1
while spiel == 1 : 
    e_name = input("Bist du sicher dass "+ name + " dein Name sein soll, hört sich irgendwie merkwürdig an. ")
    if e_name == "Ja" :
        print ("Ok")
        spiel = 0
    elif e_name == "Nein" :
        name = input("Was soll dann dein Name sein?")
    else :
        print("Antworte mir mit Ja oder Nein")

#Reiseziel
print("Ok ja passt. Hallo " +name+ " hertzlich wilkommen anbord des Schiffs Strix, gesponsort von der ASUS coopararation.\nIch sehe sie haben eine Monatskarte. Wohin soll es denn Gehen?")
e_reiseziel = int (input("1. Kaliskya\n2. Kennedyland\n3. Neureihnstadt\n"))
if e_reiseziel == 1:
    print("Na viel spaß. Ich hoffe sie haben sich was zu Essen mitgenommen? Ich hab gehört da solls wieder Wölfe geben.")
elif e_reiseziel == 2:
    print("Passen sie auf sich auf das soll raues Pflaster sein")
elif e_reiseziel == 3:
    print("""Oh ich glaube das können sie sich abschminken, auch bei den geschwindigkeiten von diesem alten Passagierschiff wird deren Hafen nicht fertig sein ehe sie da sind.
Ich denke Kennedyland und Kaliskya sind ihre einzigen Optionen. Außer sie wollen abspringen?""")
    e_reiseziel = int (input("1. Kaliskya\n2. Kennedyland"))
    if e_reiseziel == 1 or e_reiseziel == 2 :
        print("Ok, setzen sie sich.")
    elif e_reiseziel == 3 :
        print("Alles klar, wenn sie meinen dass ise das hinbekommen...setzen sie sich doch.")




