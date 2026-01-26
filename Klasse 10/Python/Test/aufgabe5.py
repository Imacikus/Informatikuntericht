class Akku:
    def __init__(self, kapazitaet):
        self.kapazitaet = kapazitaet
    
    def ist_leer(self):
        if self.kapazitaet < 5:
            print("Akku fast leer!")
        else:
            print("Akkustand ausreichend")