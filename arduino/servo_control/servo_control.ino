/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 90;    // variable to store the servo position
char readByte;
String readBuffer = "000";

void setup() {
  Serial.begin(9600);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  myservo.write(pos);
}

void loop() {

  for(int i = 0; i < 3; i++)
  {
    while(Serial.available() < 1) 
    {
    }
    readBuffer[i] = Serial.read();
  }
  Serial.println(readBuffer);
  myservo.write(readBuffer.toInt());

}



