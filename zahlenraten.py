import random

def zahl_waehlen():
    """Wählt eine zufällige Zahl zwischen 0 und 100 aus."""
    return random.randint(0, 100)

def eingabe_pruefen(eingabe):
    """Prüft, ob die Eingabe eine gültige Zahl zwischen 0 und 100 ist."""
    try:
        zahl = int(eingabe)
        if 0 <= zahl <= 100:
            return zahl
        else:
            print("Bitte geben Sie eine Zahl zwischen 0 und 100 ein!")
            return None
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl ein!")
        return None

def vergleichen(versuch, zufallszahl):
    """Vergleicht den Versuch mit der zufälligen Zahl und gibt einen Hinweis zurück."""
    if versuch == zufallszahl:
        return True
    elif versuch < zufallszahl:
        print("Die gesuchte Zahl ist höher!")
        return False
    else:
        print("Die gesuchte Zahl ist niedriger!")
        return False

def spiel_starten():
    """Startet das Zahlenratespiel und zählt die Versuche."""
    zufallszahl = zahl_waehlen()
    versuche = 0

    print("Willkommen beim Zahlenratespiel!")
    print("Ich habe eine Zahl zwischen 0 und 100 gewählt.")

    while True:
        eingabe = input("\nRaten Sie eine Zahl: ")
        versuch = eingabe_pruefen(eingabe)

        if versuch is None:
            continue

        versuche += 1
        if vergleichen(versuch, zufallszahl):
            print(f"\nGratulation! Sie haben die richtige Zahl {zufallszahl} in {versuche} Versuchen erraten!")
            break

spiel_starten()
