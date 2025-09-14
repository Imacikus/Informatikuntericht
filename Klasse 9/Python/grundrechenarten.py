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

def diferenz(a, b):
    return a - b

def produkt(a, b):
    return a * b

def devi(a, b):
    return a / b

def quadrate(a, b):
    return a**2, b**2

def reziproke(a, b):
    return 1/a, 1/b

# Werte in der Konsole abfragen
a = float(input("Zahl 1: "))
b = float(input("Zahl 2: "))

# Funktionsaufruf im Hauptprogramm
Summe = addi(a, b)
Differenz = diferenz(a, b)
Produkt = produkt(a, b)
Dividenz = devi(a, b)
Quadrat_a, Quadrat_b = quadrate(a, b)
Reziproke_a, Reziproke_b = reziproke(a, b)

# Resultat printen
print("Summe =", Summe)
print("Differenz =", Differenz)
print("Produkt =", Produkt)
print("Dividenz =", Dividenz)
print("Quadrat von Zahl 1 =", Quadrat_a)
print("Quadrat von Zahl 2 =", Quadrat_b)
print("Reziproke von Zahl 1 =", Reziproke_a)
print("Reziproke von Zahl 2 =", Reziproke_b)