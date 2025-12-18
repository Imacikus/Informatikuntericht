# schueler_class.py

class Schueler:
    def __init__(self, name, alter, groesse, klasse, hobby):
        self.name = name
        self.alter = alter
        self.groesse = groesse
        self.klasse = klasse
        self.hobby = hobby

    def __str__(self):
        status = "erwachsen" if self.alter >= 18 else "minderjährig"
        return (
            f"╔════════════════════════════════════╗\n"
            f"  STECKBRIEF: {self.name}\n"
            f"╚════════════════════════════════════╝\n"
            f"  • Klasse:  {self.klasse}\n"
            f"  • Alter:   {self.alter} Jahre ({status})\n"
            f"  • Größe:   {self.groesse:.2f}m\n"
            f"  • Hobby:   {self.hobby}\n"
            f"--------------------------------------"
        )

    def geburtstag(self):
        self.alter += 1
        # Hier printen wir nur eine kurze Info, keinen ganzen Steckbrief
        print(f"--- Info: {self.name} hatte Geburtstag! ---")

# 1. Personen erstellen
schueler1 = Schueler("Max Mustermann", 16, 1.80, "10c", "Programmieren")
schueler2 = Schueler("Max Musterfrau", 17, 1.71, "11c", "Tanzen")

# 2. Änderungen durchführen (bevor wir die Liste zeigen)
schueler2.geburtstag()
print() # Eine Leerzeile für die Optik

# 3. Jetzt die finale Liste mit genau 2 Personen ausgeben
meine_klasse = [schueler1, schueler2]

for person in meine_klasse:
    print(person)