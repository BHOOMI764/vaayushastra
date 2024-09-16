// Include Libraries
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

// Create an RF24 object
RF24 radio(9, 8);  // CE, CSN

// Address through which two modules communicate
const byte address[6] = "00001";

void setup() {
  Serial.begin(9600); // For debugging

  // Initialize the radio
  radio.begin();
  
  // Set the address for the writing pipe
  radio.openWritingPipe(address);
  
  // Set module as transmitter
  radio.setPALevel(RF24_PA_MIN); // Optional: Adjust power level if needed
  radio.stopListening(); // Ensure we are in transmit mode
  
  Serial.println("Radio initialized.");
}

void loop() {
  // Data to send
  const int val[] = {142, 45, 78};
  
  // Send data to receiver
  bool success = radio.write(&val, sizeof(val));
  
  // Check if the data was sent successfully
  if (success) {
    Serial.println("Data sent successfully.");
  } else {
    Serial.println("Data send failed.");
  }
  
  delay(1000); // Wait for a second before sending the next packet
}



