#define PIN_LED 13

byte msg[] = {
  'p', 'i', 'n', 'g', '\n'
};

long long lastSendMillis;

void setup() {
  pinMode(PIN_LED, OUTPUT);
  Serial.begin(115200);
  lastSendMillis = millis();
}

void loop() {
  if (millis() > lastSendMillis + 600) {
    lastSendMillis = millis();
    digitalWrite(PIN_LED, HIGH);
    //Serial.write(msg, 5);
    digitalWrite(PIN_LED, LOW);
  }

  if (Serial.available()) {
    int rv = Serial.read();
    if (rv == 'p' || rv == 'n') {
      Serial.write(rv - 32);
    }
    else if (rv == 'i') {
      Serial.write('O');
    }
    else if (rv == 'g') {
      Serial.write('G');
      Serial.println(millis());
      //Serial.write('\n');
    }
  }
}


