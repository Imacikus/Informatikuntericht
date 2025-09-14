# Median berechnen

num = []                                    # leere Liste erzeugen

for i in range(1, 8):                       # die Werte von 1 bis 7 hinzunehmen
    num.append(i)

num.sort()                                  

median = num[len(num) // 2]

print("Die Zahlen:")
print(num)
print("Median: ",median)                               # Print vom Median
