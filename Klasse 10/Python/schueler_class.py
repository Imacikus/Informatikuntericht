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
        