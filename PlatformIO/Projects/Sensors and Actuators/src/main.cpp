#include <Arduino.h>

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println(analogRead(A0));
  int mappednum = map(analogRead(A0), 0,680 , 0, 255);
  analogWrite(9, mappednum);
  delay(100);
}