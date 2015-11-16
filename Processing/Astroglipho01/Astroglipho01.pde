String s = "Hello World";

void setup() {
  size(400, 400);
  fill(0);
  smooth();
}

void draw() {
  background(255);
  for (int i=0; i<s.length(); i++) {
    char c = s.charAt(i);
    textSize(16+i*2);
    for (float j=0; j<TWO_PI; ) {
      pushMatrix();
      translate(width/2, height/2);
      rotate(j);
      translate(0, 16+i*16);
      text(c, 0, 0);
      popMatrix();
      j += PI/(6+i*4);
    }
  }
}