import math  # Mathpaket importieren

for radius in range(1, 11):
    AKugel = 4 * math.pi * radius ** 2
    print(f"Radius: {radius} : A = {AKugel:.2f}")
