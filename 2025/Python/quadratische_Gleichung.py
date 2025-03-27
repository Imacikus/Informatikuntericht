# Ziel des Programms: Lösen einer quadratischen Gleichung
# Dieser Code wurde von Linus Kropeit am 27. März 2025 geschrieben


import math                             # Mathe Bibliothek importieren

a = float(input('a: '))                 # Variable a abfragen
b = float(input('b: '))                 # Variable b abfragen
c = float(input('c: '))                 # Variable c abfragen

#Diskriminante berechnen
diskriminante = b**2 - 4*a*c            

if diskriminante > 0:                                           #Diskriminante größer als 0?
    x1 = (-b + math.sqrt(diskriminante)) / (2 * a)              #ja: x1 und x2 berechnen
    x2 = (-b - math.sqrt(diskriminante)) / (2 * a)
    print(f"Die Lösungen sind x1 = {x1} und x2 = {x2}")         #Ergebnisse ausgeben

elif diskriminante == 0:                                        #Diskriminante gleich 0?
    x1 = -b / (2 * a)                                           #ja: x1 berechnen
    print(f"Es gibt eine doppelte Lösung: x1 = {x1}")

else:
    print('Es gibt keine reelle Lösung')                        #nein: keine Lösung Ausgeben


