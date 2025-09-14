import math

# Formatierung des Platbedarfs
# Erstelle Tabellenkopf
print("Zahl\tWurzel")
print("_"*15)

# Schleife über einige Zahlen mit formatierter Ausgabe
# derQuadratwurzel
for i in range(0, 26):
    sqi = math.sqrt(i)
    # Format 2d: ganze Zahl (d) mit zwei Stellen (2)
    # Format 7.12f: insgesamt 7 stellen mit 12 Nachkommastelleneiner Gleitkommazahl
    print(f"{i:2d}\t{sqi:7.12f}")