from statistics import median  # Medianfunktion importieren

# Ursprüngliche unsortierte Liste
liste = [181, 187, 196, 196, 198, 203, 207, 211, 215]

# Listen sortieren
liste_aufsteigend = sorted(liste)           # Aufsteigend sortieren
liste_absteigend = sorted(liste, reverse=True)  # Absteigend sortieren

# Median berechnen
median_wert = median(liste)

# Ergebnisse ausgeben
print("Aufsteigend sortiert:", liste_aufsteigend)
print("Absteigend sortiert:", liste_absteigend)
print("Median:", median_wert) 