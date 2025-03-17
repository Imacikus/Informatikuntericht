#17. März 2025
#Das Programm berechnet anhand des radius den Umfang und die Kreisfläche eines Kreises

import math         #Mathpaket importieren

print('Dieses Programm berechnet den Umfang + die Kreisfläche.')
radius = int(input("\nGebe zunächst den Radius des Kreises an: "))
umfang = 2 * radius * math.pi           #Umfang berechnen
durchmesser = 2 * radius                #Durchmesser berechnen
kreisflaeche = math.pi * radius ** 2    #Kreisfläche berechnen

print()
print('Werte:')
print('Umfang       : ', umfang)
print('Durchmesser  : ', durchmesser)
print('Kreisfläche  : ', kreisflaeche)