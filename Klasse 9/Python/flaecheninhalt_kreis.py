import math  # Mathpaket importieren

for radius in range(1, 11):
    A = math.pi * radius**2
    V = (4/3) * math.pi * radius**3
    print(f"Radius: {radius} : A = {A:.2f} : V = {V:.2f}")
