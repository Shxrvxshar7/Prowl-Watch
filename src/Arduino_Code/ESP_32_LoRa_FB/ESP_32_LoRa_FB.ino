
// GDSC



#include <Arduino.h>
#include <WiFi.h>
#include <Firebase_ESP_Client.h>

//Provide the token generation process info.
#include "addons/TokenHelper.h"
//Provide the RTDB payload printing info and other helper functions.
#include "addons/RTDBHelper.h"

#include <SPI.h>
#include <LoRa.h>
//#include <Wire.h>
#include "LiquidCrystal_I2C.h"

#define BUZZ 13

/*-------- FIREBASE SECTION ------------*/

// Insert your network credentials
#define WIFI_SSID "Onichan"
#define WIFI_PASSWORD "callme@9"

// Insert Firebase project API Key
#define API_KEY "AIzaSyBbC7827l2Y6n5GpKtZP5j2i3W6kTno6AI"

// Insert RTDB URLefine the RTDB URL */
#define DATABASE_URL "https://forest-v1-c853f-default-rtdb.asia-southeast1.firebasedatabase.app/" 

//Define Firebase Data object
FirebaseData fbdo;

FirebaseAuth auth;
FirebaseConfig config;

unsigned long sendDataPrevMillis = 0;
int count = 0;
bool signupOK = false;

/*-------- LORA SECTION ------------*/
#define ss 5
#define rst 14
#define dio0 2

// LCD declaration

LiquidCrystal_I2C lcd(0x27,16,2);

String data;
void setup() {

  Serial.begin(115200);

  // LoRa Section
  while (!Serial);
  LoRa.setPins(ss, rst, dio0);
  Serial.println("LoRa Receiver");

  if (!LoRa.begin(433E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }

  
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    delay(300);
  }
  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();

  /* Assign the api key (required) */
  config.api_key = API_KEY;

  /* Assign the RTDB URL (required) */
  config.database_url = DATABASE_URL;

  /* Sign up */
  if (Firebase.signUp(&config, &auth, "", "")){
    Serial.println("ok");
    signupOK = true;
  }
  else{
    Serial.printf("%s\n", config.signer.signupError.message.c_str());
  }

  /* Assign the callback function for the long running token generation task */
  config.token_status_callback = tokenStatusCallback; //see addons/TokenHelper.h
  
  Firebase.begin(&config, &auth);
  Firebase.reconnectWiFi(true);


// LCD Declaration and PC Buzzer
  lcd.init();
  pinMode(BUZZ,OUTPUT);
}

void loop() {
  
   int packetSize = LoRa.parsePacket();
  
  
  if (packetSize) {
    lcd.clear();
    // received a packet

    // read packet
    while (LoRa.available()) {
     
      data = (LoRa.readString());
    }

    // print RSSI of packet
    
    Serial.println("Received data as string: ");
    Serial.print(data);
    Serial.print("' with RSSI ");
    Serial.println(LoRa.packetRssi());

    lcd.setCursor(0,0);
    lcd.print("Data Received!");
    lcd.setCursor(0,1);
    lcd.print(data);

    digitalWrite(BUZZ,HIGH);

    if (Firebase.ready() && signupOK)
    {
     sendDataPrevMillis = millis();
     // Write an Int number on the database path test/int
    if (Firebase.RTDB.setInt(&fbdo, "Base/persons", 1))
    {
      Serial.println("PASSED");
      Serial.println("PATH: " + fbdo.dataPath());
      Serial.println("TYPE: " + fbdo.dataType());
    }
    else 
    {
      Serial.println("FAILED");
      Serial.println("REASON: " + fbdo.errorReason());
    }
    
    
    // Write an Float number on the database path test/float
    if (Firebase.RTDB.setString(&fbdo, "Node/Camera", data))
    {
      Serial.println("PASSED");
      Serial.println("PATH: " + fbdo.dataPath());
      Serial.println("TYPE: " + fbdo.dataType());
    }
    else
     {
      Serial.println("FAILED");
      Serial.println("REASON: " + fbdo.errorReason());
    }

    if (Firebase.RTDB.setString(&fbdo, "Node/Time", data))
    {
      Serial.println("PASSED");
      Serial.println("PATH: " + fbdo.dataPath());
      Serial.println("TYPE: " + fbdo.dataType());
    }
    else
     {
      Serial.println("FAILED");
      Serial.println("REASON: " + fbdo.errorReason());
    }
    }
  }

  digitalWrite(BUZZ,LOW);

  

}
