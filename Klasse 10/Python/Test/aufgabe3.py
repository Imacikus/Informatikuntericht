class Handy:
    def __init__(self, marke, akku, besitzer):
        self.marke = marke
        self.akku = akku
        self.besitzer = besitzer

    def aufladen(self):
        self.akku = 10
        print(f"Akku aufgeladen: {self.akku}%")