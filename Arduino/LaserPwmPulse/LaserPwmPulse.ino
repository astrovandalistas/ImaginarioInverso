int LED_PIN = 9;
int LASER_PIN = 13;
int transDuration = 1500;

void setup() {}

void loop() {
  if ((millis() / transDuration) % 3 != 0) {
    analogWrite(LED_PIN, 255);
    analogWrite(LASER_PIN, 255);
    delay(random(32, 128));
    analogWrite(LED_PIN, 0);
    analogWrite(LASER_PIN, 0);
    delay(random(32, 128));
  }
  else {
    analogWrite(LED_PIN, 0);
    analogWrite(LASER_PIN, 0);
    delay(100);
  }
}


