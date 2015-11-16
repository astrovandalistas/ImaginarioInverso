String s = "Hello World";
int I_OFFSET = 8;
int C_OFFSET = 2;

void setup() {
  size(400, 400);
  strokeWeight(2);
  noFill();
  smooth();
}

void draw() {
  background(255);
  for (int i=0; i<s.length(); i++) {
    char c = s.charAt(i);
    for (int j=0; j<8; j++) {
      if ((c>>j&0x1) == 1) {
        stroke(0);
      } else {
        stroke(255);
      }
      int r=I_OFFSET+i*8*C_OFFSET+j*C_OFFSET;
      ellipse(width/2, height/2, r*2, r*2);
    }
  }
}