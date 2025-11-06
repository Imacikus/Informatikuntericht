# schueler_class.py

class Schueler:
    # Klasse für einen Schüler mit Name, Alter, Größe, Hobby und Niveau
    def __init__(self, name, alter, groesse, klasse, hobby):
        self.name = name
        self.alter = alter
        self.groesse = groesse
        self.klasse = klasse
        self.hobby = hobby

    def vorstellen(self):
        print(f"Hallo, ich bin {self.name}.")
        print(f"Ich bin {self.alter} Jahre alt.")
        print(f"Ich bin {self.groesse}m groß.")
        print(f"Ich bin in der Klasse {self.klasse}.")
        print(f"Mein Hobby ist {self.hobby}.")
        print()

    def geburtstag(self):
        self.alter += 1
        print(f"Alles Gute zum Geburtstag, {self.name}! 🎉")
        print(f"Du bist jetzt {self.alter} Jahre alt.\n")


# Instanzen erstellen
schueler1 = Schueler("Max Mustermann", 16, 1.80, "10c", "Programmieren")
schueler2 = Schueler("Max Musterfrau", 15, 1.71, "11c", "Tanzen")

# Methoden aufrufen
schueler1.vorstellen()
schueler2.vorstellen()

# Geburtstag
schueler1.geburtstag()
schueler2.geburtstag()
