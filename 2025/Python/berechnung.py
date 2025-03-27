#Variablen festlegen
a = int(input("\na: "))
b = int(input("\nb: "))
c = int(input("\nc: "))
d = int(input("\nd: "))
e = int(input("\ne: "))
f = int(input("\nf: "))

#Berechnungen
D = a*d - b*c
D1 = d*e - b*f
D2 = a*f - c*e

if D != 0:                          #Nenner gleich Null?
    
    x = D1/D                        #ja: berechne x
    y = D2/D                        #berechne y

    print('x =', x)                 #Ergebnisse ausgeben
    print('y =', y)

#Fehlermeldung ausgeben
else:                               
    print()
    print('***** Division durch Null *****')
    print('===============================')
    print()
    print('Das lineare Gleichungssystem')
    print('hat keine Loesung.')
    
