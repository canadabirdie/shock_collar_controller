#include <SoftwareSerial.h>

SoftwareSerial mySerialOut(9, 10, true);

void setup() {
  Serial.begin(9600);
  pinMode(10, OUTPUT);
}

//uint8_t test[24] = {255, 248, 142, 142, 232, 136, 136, 142, 142, 136, 136, 136, 136, 232, 142, 232, 136, 238, 238, 142, 136, 142, 136, 128};
const int zero = 254;
const int one = 128;
const int inputLen = 42;
uint8_t input[42] = {zero, one, zero, one, one, zero, zero, zero, zero, zero, zero, one, zero, one, zero, zero, zero, zero, zero, zero, zero, zero, one, zero, zero, one, one, zero, zero, zero, one, one, one, one, zero, one, zero, zero, zero, one, zero, zero};

void loop() {
  if (Serial.available() > 0) {
    for (int i = 0; i < inputLen; i++) {
      while (!Serial.available()) {}
      int c = Serial.read();
      switch (c) {
        case 48: input[i] = zero; break;
        case 49: input[i] = one; break;
        default: Serial.println("Something went wrong");
      }
    }
    for (int i = 0; i < 10; i++) {
      if (Serial.available() > 0) {
        break;
      }
      digitalWrite(10, HIGH);
      delayMicroseconds(1300);
      digitalWrite(10, LOW);
      delayMicroseconds(700);
      mySerialOut.begin(8000);
      mySerialOut.write(input, 42);
      mySerialOut.end();
      delay(20);
    }
  }
}
