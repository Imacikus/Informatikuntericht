import random

# Kategorien und Wörter
kategorien = {
    "Tiere": ["Hund", "Katze", "Löwe", "Elefant", "Giraffe", "Panda", "Eule", "Fuchs"],
    "Schule": ["Informatik", "Mathe", "Physik", "Chemie", "Biologie", "Geschichte", "Deutsch", "Sport"],
    "Sport": ["Fußball", "Basketball", "Tennis", "Schwimmen", "Laufen", "Radfahren", "Hockey", "Volleyball"],
    "Essen": ["Pizza", "Burger", "Nudeln", "Salat", "Kuchen", "Eis", "Suppe", "Brot"]
}

# ASCII-Art für den Galgen
galgen_stufen = [
    """
     ------
     |    |
     |
     |
     |
     |
    -----
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    -----
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    -----
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    -----
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    -----
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    -----
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    -----
    """
]

def wort_waehlen():
    kategorie = random.choice(list(kategorien.keys()))
    wort = random.choice(kategorien[kategorie])
    return wort.upper(), kategorie

def buchstabe_pruefen(buchstabe):
    buchstabe = buchstabe.upper()
    if buchstabe.isalpha() and len(buchstabe) == 1:
        return buchstabe
    return None

def spiel_runden_anzeigen(versuche, galgen_stufen):
    print(galgen_stufen[versuche])

def spiel_starten():
    punkte = 0
    spielen = True

    while spielen:
        wort, kategorie = wort_waehlen()
        geratene_buchstaben = set()
        falsche_buchstaben = set()
        versuche = 0
        max_versuche = len(galgen_stufen) - 1

        print(f"\n--- Neue Runde ---")
        print(f"Kategorie: {kategorie}")
        print(f"Aktueller Punktestand: {punkte}")

        while versuche < max_versuche:
            spiel_runden_anzeigen(versuche, galgen_stufen)
            print(f"Wort: {' '.join([buchstabe if buchstabe in geratene_buchstaben else '_' for buchstabe in wort])}")
            print(f"Falsche Buchstaben: {' '.join(sorted(falsche_buchstaben))}")

            buchstabe = input("Rate einen Buchstaben: ").strip()
            buchstabe = buchstabe_pruefen(buchstabe)

            if buchstabe is None:
                print("Ungültiger Buchstabe. Bitte versuche es erneut.")
                continue

            if buchstabe in geratene_buchstaben or buchstabe in falsche_buchstaben:
                print("Dieser Buchstabe wurde bereits geraten. Versuche es erneut.")
                continue

            if buchstabe in wort:
                geratene_buchstaben.add(buchstabe)
                print(f"Richtig! '{buchstabe}' ist im Wort.")
                if all(b in geratene_buchstaben for b in wort):
                    punkte += 10
                    print(f"Glückwunsch! Du hast das Wort '{wort}' erraten und 10 Punkte erhalten!")
                    break
            else:
                falsche_buchstaben.add(buchstabe)
                versuche += 1
                punkte -= 1
                print(f"Falsch! '{buchstabe}' ist nicht im Wort. Du verlierst 1 Punkt.")

        if versuche == max_versuche:
            spiel_runden_anzeigen(versuche, galgen_stufen)
            print(f"Game Over! Das Wort war: {wort}")
            punkte -= 5
            print(f"Du verlierst 5 Punkte.")

        spielen = input("\nMöchtest du noch eine Runde spielen? (ja/nein): ").strip().lower() == "ja"

    print(f"\nSpiel beendet. Dein Endstand: {punkte} Punkte.")

if __name__ == "__main__":
    spiel_starten()