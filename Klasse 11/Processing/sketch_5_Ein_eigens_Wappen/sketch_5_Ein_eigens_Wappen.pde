// Sketch Size
size(500, 400);

// Grundform Wappen
strokeWeight(5);
fill(#F8CBFF);

beginShape();
vertex(250, 40);
vertex(400, 100);
vertex(370, 280);
vertex(250, 360);
vertex(130, 280);
vertex(100, 100);
endShape(CLOSE);

arc(300, 200, 50, 60,
    radians(30), radians(330));
    
arc(200, 200, 50, 60,
    radians(150), radians(210));
    
