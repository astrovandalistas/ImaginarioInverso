//String MSG = "Imaginario Inverso Narrativas Hacia el Futuro";
String MSG = "Sets the current font size. This size will be used in all subsequent calls to the text() function. Font size is measured in units of pixels";

PGraphics canvas;
int canvasSize;

// text size > 12
int TEXT_SIZE = 24;

void setup() {
  size(300, 200);
  frameRate(width*2);
  background(255);

  canvas =  createGraphics(width, height);
  canvas.beginDraw();
  canvas.textSize(TEXT_SIZE);
  canvas.textLeading(TEXT_SIZE);
  canvas.fill(0);
  canvas.background(255);
  canvas.text(MSG, 0, 0, width, height);
  canvas.endDraw();
  canvasSize = canvas.width*canvas.height;
  canvas.loadPixels();
}

void draw() {
  if (frameCount%canvas.width == 0) {
    println(frameRate);
  }

  int x = (frameCount%canvasSize)%canvas.width;
  int y = (frameCount%canvasSize)/canvas.width;
  int ym1 = max(0, y-1);
  int yp1 = min(canvas.height-1, y+1);

  if ((canvas.pixels[y*canvas.width+x]&0xff) < 200) {
    stroke(200, 0, 0);
    fill(200, 0, 0);
    ellipse(x, y, 1, 1);
    //point(x, y);
  }

  if ((canvas.pixels[yp1*canvas.width+x]&0xff) < 200) {
    stroke(200, 0, 0);
    fill(200, 0, 0);
    ellipse(x, yp1, 1, 1);
    //point(x, yp1);
  }

  if ((canvas.pixels[ym1*canvas.width+x]&0xff) < 200) {
    stroke(0);
    fill(0);
    ellipse(x, ym1, 1, 1);
    //point(x, ym1);
  }
}