class Handy:
    def __init__(self, marke, modell, akku):
        self.marke = marke
        self.modell = modell
        self.akku = akku
    
    def laden(self):
        self.akku = 100
    
    def informationen(self):
        print(f"Marke: {self.marke}")
        print(f"Modell: {self.modell}")
        print(f"Akku: {self.akku}%")
        print("---")

# Zwei Handy-Objekte erstellen
handy1 = Handy("Apple", "iPhone 14", 50)
handy2 = Handy("Samsung", "Galaxy S23", 30)

# Handy 1 laden
handy1.laden()

# Informationen ausgeben
print("Handy 1:")
handy1.informationen()

print("Handy 2:")
handy2.informationen()