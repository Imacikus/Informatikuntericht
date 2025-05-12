# Umrechnung von Temperaturen

# Celsius2Fahrenheit
# Aufgabe       Berechnet die Temperatur in Grad Fahrenheit
# Input:        T = Temperatur in Grad Celsius
# Output:       Temperatur in Grad Fahrenheit
def Celsius2Fahrenheit(T):
    F = T * 9 / 5 + 32  # berechne Temperatur in Fahrenheit
    return F

# Fahrenheit2Celsius
# Aufgabe       Berechnet die Temperatur in Grad Celsius
# Input:        T = Temperatur in Grad Fahrenheit
# Output:       Temperatur in Grad Celsius
def Fahrenheit2Celsius(T):
    C = (T - 32) * 5 / 9  # berechne Temperatur in Celsius
    return C

# Auswahl der Umrechnung
wahl = input("Möchten Sie Fahrenheit (f) oder Celsius (c) berechnen? ").strip().lower()

if wahl == 'f':
    C1 = float(input("Bitte die Temperatur in Grad Celsius eingeben: "))  # Eingabe von der Tastatur
    F2 = Celsius2Fahrenheit(C1)  # berechne Fahrenheit
    print(C1, "Grad Celsius =", F2, "Grad Fahrenheit")
elif wahl == 'c':
    F1 = float(input("Bitte die Temperatur in Grad Fahrenheit eingeben: "))  # Eingabe von der Tastatur
    C2 = Fahrenheit2Celsius(F1)  # berechne Celsius
    print(F1, "Grad Fahrenheit =", C2, "Grad Celsius")
else:
    print("Error")