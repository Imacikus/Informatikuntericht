# Tabellenkopf
print("Zahl\tQuadrat\t \t Kubik")

for i in range(0, 26):
    Quadrat = i**2
    ku = i**3
    print(f"{i:2d}\t{Quadrat:7f}\t{ku:7f}")