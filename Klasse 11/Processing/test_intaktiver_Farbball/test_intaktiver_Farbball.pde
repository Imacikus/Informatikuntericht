int ballgroesse = 50;
int ballfarbeRot = 100;
int ballfarbeGruen = 100;

void setup() {
  size(1200, 800);
  
  stroke(0);
  strokeWeight(3);
}



// Ball folgt dem Mauszeiger und veräändert seine Farbe
void draw() {
  background(255);
  ballfarbeRot = mouseX * 255 / width;
  ballfarbeGruen = mouseY * 255 / height;


  fill(ballfarbeRot, ballfarbeGruen, 100);
  ellipse(mouseX, mouseY, ballgroesse, ballgroesse);
}

// Ball wird bei Mausklick größer,
void mousePressed() {
  ballgroesse += 10;
}
// Ball wird bei Tstendruck zurückgesetzt
void keyPressed() {
  ballgroesse = 50;
} 
