# Beispiel einer Funktion in Python

# Definition der Funktion addi
# !!!!! Muss vor dem Aufruf der Funktion im Quelltext stehen !!!!!

# Name:             addi
# Aufgabe:          Addiert zwei Werte.
# Input:            a = 1. Summand
#                   b = 2. Summand
# Output            a + b
def addi(a, b):
    return a + b

# Werte in der Konsole abfragen
a = float(input("Summand 1: "))
b = float(input("Summand 2: "))

# Funktionsaufruf im Hauptprogramm
Summe = addi(a, b)

# Resultat printen
print("Ergebnis Addition =", Summe)