#include <Arduino.h>
#define redButton 2
#define blueButton 3
#define greenButton 4
#define yellowButton 5
#define redLED 8
#define blueLED 9
#define greenLED 10
#define yellowLED 11
#define redRGB 12
#define greenRGB 13
#define MAX_PATTERN_LENGTH 100
int current_pattern_length = 1;
 
int challenge[MAX_PATTERN_LENGTH];
int response[MAX_PATTERN_LENGTH];
int recorded;
int score;
void setup() {
 // Set up pin mode for each LED and button.
  pinMode(redButton, INPUT);
  pinMode(blueButton, INPUT);
  pinMode(greenButton, INPUT);
  pinMode(yellowButton, INPUT);

  pinMode(redLED, OUTPUT);
  pinMode(blueLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(yellowLED, OUTPUT);

  pinMode(redRGB, OUTPUT);
  pinMode(greenRGB, OUTPUT);

  // Ensure LEDs off initially
  digitalWrite(redLED, LOW);
  digitalWrite(blueLED, LOW);
  digitalWrite(greenLED, LOW);
  digitalWrite(yellowLED, LOW);
  digitalWrite(redRGB, LOW);
  digitalWrite(greenRGB, LOW);

  // initialize game state
  score = 0;
  recorded = 0;

  // seed RNG using an analog pin
  randomSeed(analogRead(A0));

  Serial.begin(9600);

  // Flash the RGB LED red and green
  for (int i = 0; i < 5; i++) {
    digitalWrite(greenRGB, HIGH);
    digitalWrite(redRGB, LOW);
    delay(100);
    digitalWrite(greenRGB, LOW);
    digitalWrite(redRGB, HIGH);
    delay(100);
  }
  // Turn the RGB LED off
  digitalWrite(greenRGB, LOW);
  digitalWrite(redRGB, LOW);
  // Create the challenge to store in the array
  for (int i = 0; i < MAX_PATTERN_LENGTH; i++) {
    // pick a random LED pin#
    // Hint: What numbers are the LED pins connected to?
    challenge[i] = random(8,12);
    Serial.println(challenge[i]);
  }
}

/*
  This function will display the first
  'current_pattern_length' LEDs of the challenge pattern
*/
void issueChallenge() {
  // using a for loop, flash the first 'current_pattern_length' entries of the 'challenge' array
  for (int i = 0; i < current_pattern_length; i++) {
    digitalWrite(challenge[i], HIGH);
    delay(600);
    digitalWrite(challenge[i], LOW);
    delay(300);
  }
}

/*
  This function compares the challenge array and the response array.
  If the user has inputted the correct sequence, the function will return true.
  If the user has inputted the incorrect sequence, the function will return false.
*/
bool isPlayerCorrect() {
  for (int i = 0; i < current_pattern_length; i++) {
    if (challenge[i] != response[i]) {
      // Player has inputted the incorrect sequence.
      return false;
    }
  }
  // Player has inputted the correct sequence.
  return true;
}

/*
  This function will wait for a user to push a button.
  When the user has pressed the button, this function
  will return the pin number of the pressed button.
*/
int get_one_button() {
  while (true) {
    if (digitalRead(redButton)) {
      // wait for release to avoid multiple detections
      while (digitalRead(redButton)) { delay(10); }
      return redLED;
    }
    if (digitalRead(blueButton)) {
      while (digitalRead(blueButton)) { delay(10); }
      return blueLED;
    }
    if (digitalRead(greenButton)) {
      while (digitalRead(greenButton)) { delay(10); }
      return greenLED;
    }
    if (digitalRead(yellowButton)) {
      while (digitalRead(yellowButton)) { delay(10); }
      return yellowLED;
    }
  }
}

void loop() {

  delay(1200);
  issueChallenge();
  // Reset number of recorded inputs
  recorded = 0;
  while (recorded != current_pattern_length) {
    response[recorded] = get_one_button();

    // Flash the LED that was just recorded
    digitalWrite(response[recorded], HIGH);
    delay(300);
    digitalWrite(response[recorded], LOW);
    delay(100);

    recorded++;
  }

  if (isPlayerCorrect()) { // The Player has inputted the correct sequence
    // Make the green LED flash 5 times with a for loop
    for (int i = 0; i < 5; i++) {
      digitalWrite(greenRGB, HIGH);
      delay(200);
      digitalWrite(greenRGB, LOW);
      delay(200);
    }
    // Player was correct so increase their score by 1
    score++;
    // Increase pattern length
    if (current_pattern_length < MAX_PATTERN_LENGTH) {
      current_pattern_length++;
    }
  }
  else { // The Player has inputted the incorrect sequence
    // Make the red LED flash 5 time using a for loop
    for (int i = 0; i < 5; i++) {
      digitalWrite(redRGB, HIGH);
      delay(200);
      digitalWrite(redRGB, LOW);
      delay(200);
    }
    // Display the score the Player got
    Serial.println("Game over!");
    Serial.print("Score: ");
    Serial.println(score);
    // Reset score and challenge length
    score = 0;
    current_pattern_length = 2;
  }
}