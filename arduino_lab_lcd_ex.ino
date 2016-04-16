/*
  LiquidCrystal Library - Serial Input

  Demonstrates the use a 16x2 LCD display.  The LiquidCrystal
  library works with all LCD displays that are compatible with the
  Hitachi HD44780 driver. There are many of them out there, and you
  can usually tell them by the 16-pin interface.

  This sketch displays text sent over the serial port
  (e.g. from the Serial Monitor) on an attached LCD.

  The circuit:
   LCD RS pin to digital pin 12
   LCD Enable pin to digital pin 11
   LCD D4 pin to digital pin 5
   LCD D5 pin to digital pin 4
   LCD D6 pin to digital pin 3
   LCD D7 pin to digital pin 2
   LCD R/W pin to ground
   10K resistor:
   ends to +5V and ground
   wiper to LCD VO pin (pin 3)

  Library originally added 18 Apr 2008
  by David A. Mellis
  library modified 5 Jul 2009
  by Limor Fried (http://www.ladyada.net)
  example added 9 Jul 2009
  by Tom Igoe
  modified 22 Nov 2010
  by Tom Igoe

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/LiquidCrystalSerial
*/

// include the library code:
#include <LiquidCrystal.h>
#include <avr/interrupt.h>
// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28);
int __counter = 0;


//arduino runs the setup function first, then the loop function below
void setup() {
  pinMode(24, OUTPUT); //K
  pinMode(26, OUTPUT); //A
  pinMode(54, OUTPUT); //VSS
  pinMode(52, OUTPUT); //VDD
  pinMode(50, OUTPUT); //Contrasty pin

  // digitalWrite(50, LOW);
  digitalWrite(24, LOW); //Backlight
  digitalWrite(26, HIGH); //Backlight
  digitalWrite(54, LOW); //GND
  digitalWrite(52, HIGH); //VDD
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // initialize the serial communications:
  Serial.begin(9600);
  // Timer0 is used for millis() - we'll just interrupt
  // in the middle and call the compA
  OCR0A = 0x01;
  TIMSK0 |= _BV(OCIE0A);
}

SIGNAL(TIMER0_COMPA_vect) 
{
   __counter++;
   if (__counter > 14){
      digitalWrite(50,HIGH);
      __counter = 0;
   }
   else if (__counter > 3){
      digitalWrite(50, LOW);
   }
}
int time[4];
unsigned int mill;

void start() {
  mill = millis();
  time[3] += mill % 1000;
  if (time[3] > 999) {
    time[2]++; 
    time[3] = time[3] % 1000;
  }
  time[2] += mill/1000;
  if (time[2] > 59) {
    time[1]++;
    time[2] = time[2] % 60;
  }
  time[1] += mill/60000;
  if (time[1] > 59) {
    time[0]++;
    time[1] = time[1] % 60;
  }
  time[0] += mill/3600000;
  if (time[0] > 23) {
    time[0] = 0;
  }
  for (int i = 0; i < 4; i++) {
      Serial.println(time[i]);
    }
}

bool init2;
//Here is where your code goes. Arduino runs this function in an infinite loop after running the setup function
void loop() {
  init2 = false;
  //return cursor to starting position
  lcd.home();

  //clear the lcd screen
  if (mill % 1000 == 0) {
    lcd.clear();
  }


  String message = Serial.readString();// read a string sent from the computer
  Serial.println(message);

  bool started = false;

  if (message.indexOf('t') == 0) {
    String hour = message.substring(1,3);
    String minute = message.substring(3,5);
    time[0] = hour.toInt();
    time[1] = minute.toInt();
    time[2] = 0;
    time[3] = 0;
    for (int i = 0; i < 4; i++) {
      Serial.println(time[i]);
    }
    init2 = true;
  }
  else if (message == "start") {
    started = true;
  }
  else if (message == "stop") {
    started = false;
  }
  else if (message == "display") {
    Serial.println("test");
    for (int i = 0; i < 3; i++) {
      lcd.print(String(time[i]) + ":");
      Serial.print(String(time[i]) + ":");
    }
    lcd.print(String(time[3]));
    Serial.print(String(time[3]));
  }
  if (started){
    start();
  }

  if (!init2) {
    lcd.print("1200");
  }
  //sleep for 1 second
}


