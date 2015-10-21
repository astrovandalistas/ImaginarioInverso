void setup() {
  Serial.begin(115200);
}

void loop() {
  if (Serial.available()) {
    int rv = Serial.read();
    Serial.write(rv);
  }
}


