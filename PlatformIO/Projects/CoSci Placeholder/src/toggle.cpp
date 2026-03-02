// #include <Arduino.h>
//
// #define LED_PIN 8
// #define BUTTON_PIN 7
//
//
// byte lastButtonState = HIGH;
// byte ledState = LOW;
//
//
// void setup() {
//     pinMode(LED_PIN, OUTPUT);
//     pinMode(BUTTON_PIN, INPUT_PULLUP);
//     Serial.begin(9600);
// }
// void loop() {
//     byte buttonState = digitalRead(BUTTON_PIN);
//     if (digitalRead(BUTTON_PIN)!=lastButtonState) {
//         Serial.println("Button state changed");
//         lastButtonState = buttonState;
//         delay(10);
//         if (digitalRead(LED_PIN)==HIGH) {
//             Serial.println("LED off");
//             digitalWrite(LED_PIN, LOW);
//         }
//         else {
//             Serial.println("LED on");
//             digitalWrite(LED_PIN, HIGH);
//         }
//     }
// }