// #include <Arduino.h>
// #define redButton 2
// #define blueButton 3
// #define greenButton 4
// #define yellowButton 5
// #define redLED 8
// #define blueLED 9
// #define greenLED 10
// #define yellowLED 11
// #define redRGB 12
// #define greenRGB 13
//
// void setup() {
//     pinMode(redButton, INPUT);
//     pinMode(blueButton, INPUT);
//     pinMode(greenButton, INPUT);
//     pinMode(yellowButton, INPUT);
//     pinMode(redLED, OUTPUT);
//     pinMode(blueLED, OUTPUT);
//     pinMode(greenLED, OUTPUT);
//     pinMode(yellowLED, OUTPUT);
//     pinMode(redRGB, OUTPUT);
//     pinMode(greenRGB, OUTPUT);
//     Serial.begin(9600);
// }
//
// void loop() {
//     bool redPressed    = digitalRead(redButton);
//     bool bluePressed   = digitalRead(blueButton);
//     bool greenPressed  = digitalRead(greenButton);
//     bool yellowPressed = digitalRead(yellowButton);
//
//     if (redPressed) {
//         digitalWrite(redLED, HIGH);
//     }
//     else {
//         digitalWrite(redLED, LOW);
//     }
//
//     if (bluePressed) {
//         digitalWrite(blueLED, HIGH);
//     }
//     else {
//         digitalWrite(blueLED, LOW);
//     }
//
//     if (greenPressed) {
//         digitalWrite(greenLED, HIGH);
//     }
//     else {
//         digitalWrite(greenLED, LOW);
//     }
//
//     if (yellowPressed) {
//         digitalWrite(yellowLED, HIGH);
//     }
//     else {
//         digitalWrite(yellowLED, LOW);
//     }
//
//     digitalWrite(redRGB, HIGH);
//     digitalWrite(greenRGB, LOW);
//     delay(150);
//     digitalWrite(redRGB, LOW);
//     digitalWrite(greenRGB, HIGH);
//     delay(150);
// }