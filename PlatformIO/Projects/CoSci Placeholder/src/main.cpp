// #include <Arduino.h>
//
// #define buttonPin 7
// #define ledPin 8
// void setup() {
//   pinMode(buttonPin, INPUT_PULLUP);
//   pinMode(ledPin, OUTPUT);
//   digitalWrite(ledPin, LOW);
// }
//
// void loop() {
//   bool buttonPressed = digitalRead(buttonPin)==LOW;
//   if (buttonPressed) {
//     Serial.println("2. Button Pressed");
//     digitalWrite(ledPin, HIGH);
//   }
//   else {
//     digitalWrite(ledPin, LOW);
//     Serial.println("2. Button Not Pressed");
//   }
// }