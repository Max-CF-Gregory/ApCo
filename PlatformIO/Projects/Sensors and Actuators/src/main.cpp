#include <Arduino.h>

const int trigPin = 10;
const int echoPin = 11;
bool state = 0;

#define button 8
#define led 12

float duration, distance;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(button, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(button)==LOW){
  	state = !state;
    if (state == 1){
      digitalWrite(led, HIGH);
    }
    else {
      digitalWrite(led, LOW);
    }
  }
  if (state == 1) {
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    duration = pulseIn(echoPin, HIGH);
    distance = (duration*.0343)/2;
    Serial.print("Distance: ");
    Serial.println(distance);
    int mappednum = map(distance, 0, 340, 0, 255);
    analogWrite(9, mappednum);
  }
  else {
    Serial.print("Potentiometer reading: ");
    Serial.println(analogRead(A0));
    int mappednum = map(analogRead(A0), 0,680 , 0, 255);
    analogWrite(9, mappednum);
  }
  Serial.print("State: ");
  Serial.println(state);
  delay(100);
}