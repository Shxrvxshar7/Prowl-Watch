# Raspberry Pi Configuration

## Components
- Raspberry pi 3 Model B
- Arduino UN0
- SX1278 LoRa Module
- PIR Sensor
- Raspberry pi cam (REV 1.3)

## Wiring

For **Arduino UNO**: 

1. Wire **SX1278 LoRa Module** to UNO by this Table:


![UNO](https://github.com/Shxrvxshar7/Prowl-Watch/assets/77162339/606624f1-bdd2-49f8-b2bf-ad6944539997)

2. Connect the **PIR Sensor** to Arduino Uno :

    - VCC of PIR to 5V of UNO
    - GND of PIR to GND of UNO
    - DO of PIR to PIN 6 of UNO

  3. Connect UNO to Raspberry pi 3 by USB
     
For **Raspberry pi**:

  Connect Pi cam to raspberry pi's cam port

## Code Configuration

### Arduino UNO

Install required libraires
  - LoRa

Open [this](/src/Arduino_Code/Uno_pi/Uno_pi.ino) code in Arduino IDE 

Select **COM PORT**,**BOARD** (here UNO) and Upload 

### Raspberry pi

Make sure you are using 'Raspian - bullseye' (latest version) without GUI
and having Python 3

1. Install **Tensorflow Lite** by referring to this [repo](https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/blob/master/deploy_guides/Raspberry_Pi_Guide.md)

2. Install **Py Serial**
   ```
   $ pip install pyserial
   ```
3. **Camera Configuration**
   ```
  $ sudo raspi-config
  # go to interface options and enable camera interface
  # reboot system to take effect
  $ sudo reboot
   ```
4. 



