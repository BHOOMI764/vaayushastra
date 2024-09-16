//Include Libraries
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

//create an RF24 object
RF24 radio(7, 8);  // CE, CSN

//address through which two modules communicate.
const byte address[6] = "00001";

void setup()
{
  while (!Serial);
    Serial.begin(9600);
  
  radio.begin();
  
  //set the address
  radio.openReadingPipe(0, address);
  
  //Set module as receiver
  radio.startListening();
}

void loop()
{
  float val[] = {0.0,0.0,0.0,0.0,0.0,0.0};
  //Read the data if available in buffer
  if (radio.available())
  {
    radio.read(&val, sizeof(val));
    Serial.println(val[0]);
    Serial.println(val[1]);
    Serial.println(val[2]);
    Serial.println(val[3]);
    Serial.println(val[4]);
    Serial.println(val[5]);
    Serial.println("-----------------------------------------------------------------------------");
  }
}
