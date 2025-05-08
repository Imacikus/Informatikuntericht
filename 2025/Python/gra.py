# Beispiel einer Funktion in Python

# Definition der Funktion addi
# !!!!! Muss vor dem Aufruf der Funktion im Quelltext stehen !!!!!

# Name:             addi
# Afugabe:          Addiert zwei Werte.
# Input:            a = 1. Summand
#                   b = 2. Summand
# Output            a + b
def addi(a, b):
    return a+ b

# Das Hauptprogramm sollte im Idealfall nur aus
# Funktionsaufrufen bestehen und falls erforderlich
# Ergebnisse printen

Summe = addi(10, 20)                        # Funktionsaufruf im Hauptprogramm
                                            # Variable Summe bekommt den Wert,
                                            # den die Funktion sum liefert.
print("Ergebnis Addition =", Summe)         # Resultat printen