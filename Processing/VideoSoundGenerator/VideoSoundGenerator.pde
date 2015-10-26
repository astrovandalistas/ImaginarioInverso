import processing.video.*;
import ddf.minim.*;
import ddf.minim.ugens.*;

Minim       minim;
AudioOutput out;
AudioRecorder recorder;

Movie movie;

Midi2Hz midi;

float lastR = 0;
float lastG = 0;
float lastB = 0; // track of the last Colors


void setup() {
  size(720, 850);
  background(0);

  minim = new Minim(this);
  out = minim.getLineOut(Minim.MONO, width);

  String fname = year()+"-"+month()+"-"+day()+"__"+hour()+"-"+minute()+"-"+second()+".wav";
  recorder = minim.createRecorder(out, fname);
  recorder.beginRecord();

  movie = new Movie(this, sketchPath("../videos/laserTease_Small.mp4"));
  movie.play();
  movie.read();

  noStroke();
}

int xmin = 0;
int xmax = 400;
int ymin = 0;
int ymax = 80;

void draw() {
  if (movie.available() == true) {
    background(0);
    movie.read(); 

    movie.loadPixels();
    movie.filter(THRESHOLD,0.9);

    float r=0;
    float g=0;
    float b=0;
    float c=0;

    for (int j = ymin; j < movie.height; j ++) {
      for (int i = xmin; i < movie.width; i ++) {
        color pixelColor = movie.pixels[j * movie.width + i];
        r += red(pixelColor);
        g += green(pixelColor);
        b += blue(pixelColor);
        c += 0.5;
      }
    }

    r = r / c;
    g = g / c;
    b = b / c;

    //if the color change then trigger the sound
    int threshold = 1;


    //using MIDI notes from 0 to 127 https://newt.phys.unsw.edu.au/jw/notes.html
    // if the last R, G, B is different by the thereshold then trigger the note
    // r%127 takes the color value from 0-255(color interval) and transforms it to 0-127 (MIDI interval)
    if (abs(lastR - r) > threshold) {
      out.playNote(0, 0.3, new ToneInstrument(Frequency.ofMidiNote(max(r%127,32)).asHz(), 0.1));
    }
    if (abs(lastG - g) > threshold) {
      out.playNote(0, 0.3, new ToneInstrument(Frequency.ofMidiNote(max(g%127,32)).asHz(), 0.1));
    }
    if (abs(lastB - b) > threshold) {
      out.playNote(0, 0.3, new ToneInstrument(Frequency.ofMidiNote(max(b%127,32)).asHz(), 0.1));
    }

    //keep Track our last color
    lastR = r;
    lastG = r;
    lastB = r;

    color averageColor = color(r, g, b);

    pushMatrix();
    translate(0, 0);
    scale(((float)width/height) * ((float)movie.width/movie.height));
    image(movie, 0, 0);
    translate(xmin, ymin);
    fill(200, 0, 0, 128);
    rect(0, 0, xmax-xmin, ymax-ymin);
    popMatrix();

    pushMatrix();
    translate(0, height/2);
    scale(((float)width/height) * ((float)movie.width/movie.height));
    fill(averageColor);
    rect(0, 0, movie.width, movie.height);
    popMatrix();
  }
}

void keyPressed() {
  if ((key == 's') && recorder.isRecording()) {
    recorder.endRecord();
    recorder.save();
  }
}

class ToneInstrument implements Instrument {
  Oscil sineOsc;

  ToneInstrument(float frequency, float amplitude) {
    sineOsc = new Oscil(frequency, amplitude, Waves.SINE);
  }

  void noteOn(float dur) {
    sineOsc.patch(out);
  }

  void noteOff() { 
    sineOsc.unpatch(out);
  }
}