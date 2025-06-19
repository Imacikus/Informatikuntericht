import math                                                 # Mathe Paket importieren

result1 = math.pow(5, 1/3)                                  # Ergebnis 1 berechnen
zwischenwert = math.pow(40, 1/3) + math.pow(135, 1/3)       # zwischenergebnis berechnen
result2 = math.pow(zwischenwert, 1/4)                       # Die Vierte Wurzel vom Zwischenergebnis berechnen

print("3te Wurzel von 5 ", result1)                         # Printen
print("Original Aufgabe ", result2)