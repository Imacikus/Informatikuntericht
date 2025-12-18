# schueler_class.py

class Schueler:
    def __init__(self, name, alter, groesse, klasse, hobby):
        self.name = name
        self.__alter = alter  # Privates Attribut
        self.groesse = groesse
        self.klasse = klasse
        self.hobby = hobby

    def __str__(self):
        """Erstellt den grafischen Steckbrief."""
        status = "erwachsen" if self.__alter >= 18 else "minderjährig"
        return (
            f"╔════════════════════════════════════╗\n"
            f"  STECKBRIEF: {self.name}\n"
            f"╚════════════════════════════════════╝\n"
            f"  • Klasse:  {self.klasse}\n"
            f"  • Alter:   {self.__alter} Jahre ({status})\n"
            f"  • Größe:   {self.groesse:.2f}m\n"
            f"  • Hobby:   {self.hobby}\n"
            f"--------------------------------------"
        )

    def geburtstag(self):
        """Erhöht das private Alter um 1."""
        self.__alter += 1
        print(f"--- Info: {self.name} hatte Geburtstag! ---")

# --- Programmablauf ---

# 1. Instanzen erstellen
schueler1 = Schueler("Max Mustermann", 16, 1.80, "10c", "Programmieren")
schueler2 = Schueler("Max Musterfrau", 17, 1.71, "11c", "Tanzen")

# 2. Logik ausführen
schueler2.geburtstag()
print() # Leerzeile

# 3. Finale Ausgabe der Liste
meine_klasse = [schueler1, schueler2]

for person in meine_klasse:
    print(person)