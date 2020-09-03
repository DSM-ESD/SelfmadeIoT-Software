/*
  AT+RENEW
  AT+RESET
  AT+TYPE0
*/
#include <SoftwareSerial.h>
SoftwareSerial BT(2, 3); // RX, TX

#define SW 10
#define BUZZER 11
#define MAX 20
String blue_str;
String str;

char command[4][MAX];
int value[4][MAX];

void setup()
{
  pinMode(SW, OUTPUT); // 스위치
  pinMode(BUZZER, OUTPUT); // 부저
  Serial.begin(9600);
  BT.begin(9600);
}

void loop()
{    
  if (BT.available()) // 블루투스로 들어온 값을 시리얼로 전송
  {
    blue_str = BT.readString();
    delay(10);

    if (blue_str == "sig1") signal_1();
    else if (blue_str == "sig2") signal_2();
    else if (blue_str == "com\r\n") comval();
    else code_set();
  }
  for (int i = 0; command[0][i]; i++)
  {
    if (command[0][i] == 'S') digitalWrite(SW, value[0][i]);
    else if (command[0][i] == 'B') digitalWrite(BUZZER, value[0][i]);
    else if (command[0][i] == 'D') delay(value[0][i]);
  }
}
