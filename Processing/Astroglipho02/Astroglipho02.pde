int LINE_WIDTH = 12;
int CHAR_SPACE = 2;
int MIN_RADIUS = 20;

void setup() {
  size(500, 400);
  noFill();
  stroke(0);
  smooth();
  strokeCap(SQUARE);
  background(255);
  drawGliph(width/4, height/2, "Ciudad");
  drawGliph(3*width/4, height/2, "Juárez");
}

void draw() {
}

void drawGliph(int x, int y, String s) {
  pushMatrix();
  translate(x, y);
  for (int i=0; i<s.length(); i++) {
    char c = s.charAt(i);
    pushMatrix();
    //rotate(i*PI/6);
    for (int j=0; j<8; j++) {
      if ((c>>j&0x1) == 1) {
        stroke(0);
      } else {
        stroke(255);
      }
      float r = i*(LINE_WIDTH+CHAR_SPACE)+MIN_RADIUS;
      float sp = PI/(20*(i+1));
      strokeWeight(LINE_WIDTH);
      arc(0, 0, 2*r, 2*r, j*TWO_PI/8, (j+1)*TWO_PI/8-sp);
    }
    popMatrix();
  }
  float r = s.length()*(LINE_WIDTH+CHAR_SPACE)+MIN_RADIUS;
  strokeWeight(2);
  stroke(0);
  ellipse(0, 0, 2*r, 2*r);
  popMatrix();
}