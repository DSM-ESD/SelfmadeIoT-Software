/*
AT+RENEW
AT+RESET
AT+TYPE0
 */
#include <SoftwareSerial.h>
SoftwareSerial BT(2, 3); // RX, TX

void setup() 
{
  pinMode(10, OUTPUT);  
  Serial.begin(9600);
  BT.begin(9600);
  Serial.println("ATcommand");
}
void loop() 
{
  if (BT.available())
  {
    char data = BT.read();
    Serial.write(data);
    if(data=='1')
    {
      digitalWrite(10, HIGH);
    }
    else if(data=='0')
    {
      digitalWrite(10, LOW);
    }
  }
  if (Serial.available())
    BT.write(Serial.read());
}
