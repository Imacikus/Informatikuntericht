#Variablen festlegen
a = 1
b = 1
c = 2
d = 2
e = 3
f = 6

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
    
