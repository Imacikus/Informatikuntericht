#schueler_class.py

class schueler:
    #Klasse für einen Schüler mit Name, Alter, Größe, Hobby

    def __init__(self, name, alter, groesse, hobby,nivau):
        self.name = name
        self.alter = alter
        self.groesse = groesse
        self.hobby = hobby
        self.nivau = nivau

    def vorstellen(self):
        print(f"Hallo ich bin {self.name}.")
        print(f"Ich bin {self.alter} Jahre alt.")
        print(f"Ich bin {self.groesse}m Groß.")
        print(f"Mein Hobby ist {self.hobby}.")
        print(f"Mein Nivau ist {self.nivau}")

# Instanzen einstellen

schueler1 = schueler("Max Mustermann", 16, 1.80, "10c", "Programmieren")
schueler2 = schueler("Max Musterfrau", 15, 1.71, "11c", "Tanzen")

schueler1.vorstellen()
schueler2.vorstellen()