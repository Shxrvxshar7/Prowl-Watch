/*  
    GDSC Solution Challenge 2023

  PV
*/

#include <SPI.h>
#include <LoRa.h>

#define PIR 6 // PIR Sensor pin

uint8_t is_motion = 0; // for motion sensor
String data;
String R_data;

void setup() 
{
  Serial.begin(9600);
  while(!Serial);

  pinMode(PIR,INPUT);

  if(!LoRa.begin(433E6))
  {
    Serial.println("LoRa Failed");
    while(1);
  }

}

void loop() {
  // Pir sensor trip
  is_motion = digitalRead(PIR);

  // data from another node
    int packetSize = LoRa.parsePacket();
    if(packetSize){
    
    Serial.print("ND:");
    while (LoRa.available())
    {
      Serial.print((char)LoRa.read());
    }
    Serial.println("");
    }

    // data to send frm pi
    if(Serial.available())
    {
      data = Serial.readString();
      LoRa.beginPacket();
      LoRa.print(data);
      LoRa.endPacket();
    }

    if(motion == 1)
    {
      Serial.println("motion");
    }

   
}
