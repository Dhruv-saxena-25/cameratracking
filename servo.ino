#include <Servo.h>

Servo verticalServo;
Servo horizontalServo;

const int vertPin = 9;
const int horzPin = 10;
int vertAngle = 90;
int horzAngle = 90;

void setup() {
  Serial.begin(9600);
  verticalServo.attach(vertPin);
  horizontalServo.attach(horzPin);
  verticalServo.write(vertAngle);
  horizontalServo.write(horzAngle);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    processCommand(command);
  }
}

void processCommand(String cmd) {
  cmd.trim();
  int commaIndex = cmd.indexOf(',');

  if (commaIndex != -1) {
    int newHorz = cmd.substring(0, commaIndex).toInt();
    int newVert = cmd.substring(commaIndex + 1).toInt();

    newHorz = constrain(newHorz, 0, 180);
    newVert = constrain(newVert, 0, 180);

    moveSmooth(horizontalServo, horzAngle, newHorz);
    moveSmooth(verticalServo, vertAngle, newVert);

    horzAngle = newHorz;
    vertAngle = newVert;
  }
}

void moveSmooth(Servo &servo, int current, int target) {
  int step = (target > current) ? 1 : -1;
  while (current != target) {
    current += step;
    servo.write(current);
    delay(15);
  }
}