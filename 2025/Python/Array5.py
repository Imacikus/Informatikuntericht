# Arithmetisches Mittel berechnen

num = []                                    # leere Liste erzeugen
sum = 0                                     # Summe ausnullen

for i in range(1, 7):                       # die Werte von 1 bis 6 hinzunehmen
    num.append(i)

for i in range(0, 6):                       # aufsummieren
    sum += num[i]

arithmetisches_mittel = sum / len(num)      # Das ganze berechnen
print(arithmetisches_mittel)                # Print vom Arithmetischen Mittel