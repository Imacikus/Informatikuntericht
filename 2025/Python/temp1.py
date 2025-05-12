# Umrechnung von Temperaturen

# Celsius2Fahrenheit
# Aufgabe       Berechnet die Temperatur in Grad Fahrenheit
# Input:        T = Temperatur in Grad Celsius
# Output:       Temperatur in Grad Fahrenheit

def Celsius2Fahrenheit(T):
    F = T * 9 / 5 + 32                                  # berechne Temperatur in Fahrenheit
    return F

# Temperatur via Tastatur abfragen
C1 = float(input("Bitte die Temperatur in Grad Celsius eingeben: "))  # Eingabe von der Tastatur
F2 = Celsius2Fahrenheit(C1)                             # berechne Fahrenheit
print(C1, "Grad Celsius =", F2, "Grad Fahrenheit")