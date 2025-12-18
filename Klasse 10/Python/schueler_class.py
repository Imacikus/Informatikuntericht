# schueler_class.py

class Schueler:
    def __init__(self, name, alter, groesse, klasse, hobby):
        self.name = name
        self.__alter = alter  # Nur das Alter ist privat (geschützt)
        self.groesse = groesse
        self.klasse = klasse
        self.hobby = hobby

    def __str__(self):
        # Intern greifen wir auf self.__alter zu
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
        # Das Alter kann nur über diese kontrollierte Methode erhöht werden
        self.__alter += 1
        print(f"--- Info: {self.name} hatte Geburtstag! ---")

    def get_alter(self):
        """Ermöglicht es, das Alter sicher auszulesen."""
        return self.__alter

# --- Test ---

schueler1 = Schueler("Max Mustermann", 16, 1.80, "10c", "Programmieren")
schueler2 = Schueler("Max Musterfrau", 17, 1.71, "11c", "Tanzen")

# 1. Geburtstag feiern (ändert das private Attribut intern)
schueler2.geburtstag()
print()

# 2. Ausgabe der Liste
meine_klasse = [schueler1, schueler2]
for person in meine_klasse:
    print(person)

# --- Erläuterung zum Zugriff ---
# print(schueler1.name)      # Funktioniert (öffentlich)
# print(schueler1.__alter)   # FEHLER! (privat)
# print(schueler1.get_alter()) # Funktioniert (über die Getter-Methode)