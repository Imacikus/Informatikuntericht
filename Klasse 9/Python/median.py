from statistics import median               # Medianfunktion importieren

#Array mit ungerader Anzahl von Elementen
#Median sollte 198 sein.

ungerade = [181, 187, 196, 196, 198, 203, 207, 211, 215]

#Array mit gerader Anzhal von Elementen
#Median sollte 200,5 sein.

gerade = [181, 187, 196, 198, 203, 207, 211, 215]

medU = median(ungerade)         #Medianwerte ausrechnen
medG = median(gerade)

print("Median ungerade Reihe =", medU)
print("Median gerade Reihe =", medG)