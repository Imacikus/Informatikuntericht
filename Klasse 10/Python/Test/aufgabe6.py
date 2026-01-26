class Kopfhörer:
    def __init__(self, marke, lautstaerke=0):
        self.marke = marke
        self.lautstaerke = lautstaerke
    
    def lauter(self):
        self.lautstaerke += 1