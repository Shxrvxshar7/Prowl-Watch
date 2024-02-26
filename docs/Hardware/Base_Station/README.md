# Base Station Configuration

## Components

**1. ESP 32** 

**2. I2c LCD Display**

**3. Buzzer**

**4. Sx1278 LoRa Module** 

## Wiring

Wire the **Sx1278** to ESP 32 according to this table:



![Wiring for SX1278](https://github.com/Shxrvxshar7/Prowl-Watch/assets/77162339/4b19b0e2-e930-494a-9327-d267e41ddc95)



Wire the **I2c LCD Display** to ESP 32 according to this table:


![I2c LCd](https://github.com/Shxrvxshar7/Prowl-Watch/assets/77162339/7d2d4af3-794b-417f-9cda-88a024dac4a7)


Wire the _+ve_ of **Buzzer** to _GPIO 13_ and _GND_ to _GND_ of ESP 32

## Code Upload
Open [this](/src/Arduino_Code/ESP_32_LoRa_FB/ESP_32_LoRa_FB.ino) code in Arduino IDE

Change the **SSID** and **PWD** to your WIFI SSID and PWD 

Change the **API_KEY** and **DATABASE_URL** to your Firebase URL 


Select the COM PORT and Choose the variant of your ESP 32 and UPLOAD
