/*
  Physical Pixel

  An example of using the Arduino board to receive data from the computer. In
  this case, the Arduino boards turns on an LED when it receives the character
  'H', and turns off the LED when it receives the character 'L'.

  The data can be sent from the Arduino Serial Monitor, or another program like
  Processing (see code below), Flash (via a serial-net proxy), PD, or Max/MSP.

  The circuit:
  - LED connected from digital pin 13 to ground through 220 ohm resistor

  created 2006
  by David A. Mellis
  modified 30 Aug 2011
  by Tom Igoe and Scott Fitzgerald

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/PhysicalPixel
*/

int incomingByte;       // a variable to read incoming serial data into
int arrivingdatabyte = 0; // initializing the incoming serial byte
const int ledPin1 = 1;  // the pin that the LED is attached to
const int ledPin2 = 2;
const int ledPin3 = 3;

const int ledPin10 = 10; // the pin that the LED is attached to
const int ledPin11 = 11;
const int ledPin12 = 12;
const int ledPin13 = 13; // the pin that the LED is attached to

void setup()
{
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);

  pinMode(ledPin10, OUTPUT);
  pinMode(ledPin11, OUTPUT);
  pinMode(ledPin12, OUTPUT);
  pinMode(ledPin13, OUTPUT);
}

void loop()
{
  // see if there's incoming serial data:
  if (Serial.available() > 0)
  {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    arrivingdatabyte = Serial.read( );  // It will read the incoming or arriving data byte  
    // if it's a capital H (ASCII 72), turn on the LED:
    Serial.println("============|incomingByte|============0======");
    Serial.println(incomingByte);
    Serial.println("============|Serial.Available|========1======");
    Serial.println(Serial.available());
    Serial.println("============|Serial.Plan|=============2======");
    Serial.println(Serial);
    Serial.println("============|Serial.Plan|=============3======");
    Serial.print("1-data byte received:");
    Serial.println(arrivingdatabyte, DEC); // here, DEC means Decimal
    Serial.print("2-data byte received:");
    Serial.println(arrivingdatabyte, HEX); // here, HEX means Decimal
    Serial.println("============|serial.Plain|============4======");
    if (incomingByte == 'H' || incomingByte == 'h')
    {
      digitalWrite(ledPin13, HIGH);
      Serial.println("pin 13 was turn on|Ardiono-13");
      digitalWrite(ledPin2, HIGH);
      Serial.println("pin 02 was turn on|Ardiono-02");
      digitalWrite(ledPin3, HIGH);
      Serial.println("pin 03 was turn on|Ardiono-03");
      digitalWrite(ledPin10, HIGH);
      Serial.println("pin 10 was turn on|Ardiono-10");
      digitalWrite(ledPin11, HIGH);
      Serial.println("pin 11 was turn on|Ardiono-11");
      digitalWrite(ledPin12, HIGH);
      Serial.println("pin 12 was turn on|Ardiono-12");
      digitalWrite(ledPin1, HIGH);
      Serial.println("pin 01 was turn on|Ardiono-01");
      Serial.println(incomingByte);
    }
    // if it's an L (ASCII 76) turn off the LED:
    else if (incomingByte == 'L' || incomingByte == 'l')
    {
      digitalWrite(ledPin1, LOW);
      Serial.println("pin 01 was turn off| Arduino-01");
      digitalWrite(ledPin2, LOW);
      Serial.println("pin 02 was turn off| Arduino-02");
      digitalWrite(ledPin3, LOW);
      Serial.println("pin 03 was turn off| Arduino-03");
      digitalWrite(ledPin10, LOW);
      Serial.println("pin 10 was turn off| Arduino-10");
      digitalWrite(ledPin11, LOW);
      Serial.println("pin 11 was turn off| Arduino-11");
      digitalWrite(ledPin12, LOW);
      Serial.println("pin 12 was turn off| Arduino-12");
      digitalWrite(ledPin13, LOW);
      Serial.println("pin 13 was turn off| Arduino-13");
      Serial.println(incomingByte);
    } else if (incomingByte != 'L' || incomingByte != 'l' || incomingByte != 'H' || incomingByte != 'h')
    {
      // Wrong-Input
      Serial.println("============|incomingByte|=========5=====");
      Serial.println("The char is a wrong command | Arduino-Z");
      Serial.println(incomingByte);
      Serial.println("============|incomingByte|=========6=====");
    }
  }
}
