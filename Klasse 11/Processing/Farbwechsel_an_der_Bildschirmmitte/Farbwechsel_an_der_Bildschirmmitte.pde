void setup() {
  size(600, 400);
  noStroke();
}

void draw() {
  background(235);
  fill(40, 150, 220); // Standardfarbe Blau

// Ergänze hier genau eine if-Anweisung.
  if (mouseY > 200) {
    fill(255, 140, 40);
  }

ellipse(mouseX, mouseY, 70, 70);
}
