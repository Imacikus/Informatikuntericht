# Maximum von 3 Integern bestimmen

a = -5                          #Werte vorgeben
b = 0
c = 44

Maximum = a                     #Schritt 1: Wert zuweisen
if b > Maximum:                 #Schritt 2: b > Maximum?
    Maximum = b                 #ja: b wird neues Maximum

if c > Maximum:                 #Schritt 3: c > Maximum?
    Maximum = c                 #ja: b wird neues Maximum

#Nun noch das Maximum ausgeben
print('Das Maximum ist: ', Maximum)