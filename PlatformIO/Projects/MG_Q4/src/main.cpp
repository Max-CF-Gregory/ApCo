#include <Arduino.h>

const int trigPin = 9;
const int echoPin = 10;
#define redLed 8
#define greenLed 11

float duration, distance;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(redLed, OUTPUT);
  pinMode(greenLed, OUTPUT);
  Serial.begin(9600);
  digitalWrite(redLed, LOW);
  digitalWrite(greenLed, LOW);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = (duration*.0343)/2;
  Serial.print("Distance: ");
  Serial.println(distance);
  if (distance<10) {
    digitalWrite(redLed, HIGH);
    digitalWrite(greenLed, LOW);
  }
  else if (10<distance<40) {
    digitalWrite(redLed, LOW);
    digitalWrite(greenLed, HIGH);
  }
  if (distance>40) {
    digitalWrite(redLed, LOW);
    digitalWrite(greenLed, LOW);
  }
  delay(250);
}