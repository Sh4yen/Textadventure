#Bibiloteken importieren
from tkinter import * 


#Inventar
inventarliste = []

#gegenstand zuum Inventar hinzufügen
def inventaradd(a):           #funktion mit parameter
    inventarliste.append(a) #Parameter kommt in die Inventarliste
inventaradd("Monatskarte")     #Argument Monatskarte wird als parameter der funktion inventar+ eigesetzt und kommt so in die liste

#spieler ruft inventar auf
def inventarrecall():
    for i in range (0, len(inventarliste), 1):  # loop mit variable i fängt bei 0 an zu zählen in 1er schritten bis zu länge der Liste definiert durch len(inventarliste)
        print(inventarliste[i])                 # i gibt die Listennummer an z.B. ist 0 gerade Monatskarte und der rest nicht definiert



#Spiel Start----------------------------------------------------------------------------------------------------------------------------------------------------

#Namenswahl
name = input("Was ist dein Name: ")
spiel = 1
while spiel == 1 : 
    e_name = input("Bist du sicher dass "+ name + " dein Name sein soll: ")
    if e_name == "Ja" :
        print ("Ok")
        spiel = 0
    elif e_name == "Nein" :
        name = input("Was soll dann dein Name sein?")
    else :
        print("Antworte mit Ja oder Nein")

#Reiseziel
print("Hallo " +name+ " hertzlich wilkommen anbord des Schiffs Strix, gesponsort von der ASUS coopararation.\nIch sehe sie haben eine Monatskarte. Wohin soll es denn Gehen?")
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


