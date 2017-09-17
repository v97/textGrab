#include "CurieIMU.h"
const int buttonPin = 2;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin
//int buttonState = 0;         // variable for reading the pushbutton status
int recordState = 0;
long firstPressTime = 0;
long lastPrintTime = 0;
const int cutOffTime = 500;

void setup() {
  Serial.begin(9600); // initialize Serial communication

  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
  
  while (!Serial);    // wait for the serial port to open

  // initialize device
  Serial.println("Initializing IMU device...");
  CurieIMU.begin();

  // Set the accelerometer range to 2G
  CurieIMU.setAccelerometerRange(2);
}

void loop() {
  float ax, ay, az;   //scaled accelerometer values

  // read accelerometer measurements from device, scaled to the configured range
  CurieIMU.readAccelerometerScaled(ax, ay, az);
  if(digitalRead(buttonPin)){
    if(recordState == 0){
      recordState = 1;
      firstPressTime = millis();
    }
    else if(recordState == 2 && (millis() - firstPressTime <= cutOffTime)){
      recordState = 4;
    }
    else if(recordState == 1 && (millis() - firstPressTime > cutOffTime)){
      recordState = 3;
    }
  }
  else if(recordState == 1){
    recordState = 2;
  }
  else if(!(recordState == 2 && (millis() - firstPressTime <= cutOffTime))){
    recordState = 0;
  }
  
  // display tab-separated accelerometer x/y/z values
  //if(millis() - lastPrintTime > 100){
    Serial.print("x,");
    Serial.print(ax);
    Serial.print(",y,");
    Serial.print(ay);
    Serial.print(",z,");
    Serial.print(az);
    Serial.print(",state,");
    Serial.print(recordState);
    Serial.println(",");
    //lastPrintTime = millis();
  //}
}
