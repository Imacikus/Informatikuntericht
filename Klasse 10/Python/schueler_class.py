# schueler_class.py

class Schueler:
    # Klasse für einen Schüler mit Name, Alter, Größe, Klasse und Hobby
    def __init__(self, name, alter, groesse, klasse, hobby):
        self.name = name
        self.alter = alter
        self.groesse = groesse
        self.klasse = klasse
        self.hobby = hobby

    def __str__(self):
        """
        Gibt eine lesbare String-Repräsentation des Schueler-Objekts zurück.
        Wird automatisch aufgerufen, z.B. bei print(objekt).
        """
        # Wir können auch self.alters_status_pruefen() in diese Methode integrieren, 
        # aber __str__ soll üblicherweise nur einen String zurückgeben, nicht direkt etwas drucken.
        # Daher halten wir uns an die reine Rückgabe der Objektattribute.
        return (f"Schüler(Name: {self.name}, Alter: {self.alter}, Größe: {self.groesse:.2f}m, "
                f"Klasse: {self.klasse}, Hobby: {self.hobby})")

    def vorstellen(self):
        print(f"Hallo, ich bin {self.name}.")
        print(f"Ich bin {self.alter} Jahre alt.")
        print(f"Ich bin {self.groesse}m groß.")
        print(f"Ich bin in der Klasse {self.klasse}.")
        print(f"Mein Hobby ist {self.hobby}.")
        
        # Altersprüfung direkt nach der Vorstellung (optional)
        self.alters_status_pruefen()
        print() # Zusätzliche Leerzeile für bessere Lesbarkeit


    def geburtstag(self):
        self.alter += 1
        print(f"Alles Gute zum Geburtstag, {self.name}! 🎉")
        print(f"Du bist jetzt {self.alter} Jahre alt.")
        
        # Altersprüfung nach dem Geburtstag
        self.alters_status_pruefen()
        print()


    def alters_status_pruefen(self):
        """Prüft und gibt den Altersstatus (erwachsen/minderjährig) aus."""
        if self.alter >= 18:
            print(f"Du bist erwachsen.")
        else:
            print(f"Du bist minderjährig.")


# Instanzen erstellen
schueler1 = Schueler("Max Mustermann", 16, 1.80, "10c", "Programmieren")
schueler2 = Schueler("Max Musterfrau", 17, 1.71, "11c", "Tanzen")

## --- NEUE AUSGABE MIT __str__ ---
print("--- String-Repräsentation mit print(objekt) ---")
print(schueler1)
print(schueler2)
print("---------------------------------------------")

print("--- Vor dem Geburtstag ---")
# Methoden aufrufen
schueler1.vorstellen() # 16 Jahre -> minderjährig
schueler2.vorstellen() # 17 Jahre -> minderjährig

print("--- Geburtstag feiern ---")
# Geburtstag
schueler1.geburtstag() # Wird 17 -> minderjährig
schueler2.geburtstag() # Wird 18 -> erwachsen

# Überprüfung nach dem Geburtstag
schueler1.vorstellen()
schueler2.vorstellen()