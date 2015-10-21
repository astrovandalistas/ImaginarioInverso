int LED_PIN = 9;
int transDuration = 3000;

void setup() {}

void loop() {
  if ((millis() / transDuration) % 3 == 0) {
    analogWrite(LED_PIN, 255);
    delay(random(32, 128));
    analogWrite(LED_PIN, 0);
    delay(random(32, 128));
  }
  else {
    analogWrite(LED_PIN, 0);
    delay(100);
  }
}


