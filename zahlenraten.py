import random

# Eine zufällige Zahl zwischen 0 und 100 generieren
zufallszahl = random.randint(0, 100)

print("Willkommen beim Zahlenratespiel!")
print("Ich habe eine Zahl zwischen 0 und 100 gewählt.")

# Solange der Benutzer noch nicht geraten hat
while True:
    # Versuchen, die Eingabe zu konvertieren
    try:
        # Eingabe des Spielers abfragen
        versuch = int(input("\nRaten Sie eine Zahl: "))
        
        # Überprüfen ob die Zahl im gültigen Bereich ist
        if versuch < 0 or versuch > 100:
            print("Bitte geben Sie eine Zahl zwischen 0 und 100 ein!")
            continue
            
        # Prüfen ob die Zahl richtig ist
        if versuch == zufallszahl:
            print(f"\nGratulation! Sie haben die richtige Zahl {zufallszahl} erraten!")
            break
        # Hinweis geben, ob die Zahl zu hoch oder zu niedrig ist
        elif versuch < zufallszahl:
            print("Die gesuchte Zahl ist höher!")
        else:
            print("Die gesuchte Zahl ist niedriger!")
            
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein!")