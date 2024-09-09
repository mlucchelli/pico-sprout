# Pico-Sprout
**Because Your Plants Don't Need the Internet to Survive - But You Do**

Monitor and automate the watering of your indoor plants using the Raspberry Pico. This MicroPython-based project analyzes soil moisture, temperature, and humidity to maintain an optimal environment for your plants. The system provides an affordable, easy-to-build solution without relying on internet connectivity.
![image](https://github.com/user-attachments/assets/9c8572e1-b782-4649-9348-3e06037e675d)

## Table of Contents

- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Hardware Setup](#hardware-setup)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)

## Getting Started
You can learn more about this project in the full [article](https://medium.com/@nosoul88/pico-sprout-because-your-plants-dont-need-the-internet-to-survive-but-you-do-17f73d3300d1).

### Components

- [Raspberry Pi Pico W](https://shop.pimoroni.com/products/raspberry-pi-pico-w?variant=40059369619539)
- [RGB Potentiometer Breakout](https://shop.pimoroni.com/products/rgb-potentiometer-breakout?variant=32236590792787)
- [1.3" SPI Colour Square LCD (240x240) Breakout](https://shop.pimoroni.com/products/1-3-spi-colour-lcd-240x240-breakout?variant=30250963632211)
- [BME280 Temperature, Pressure, Humidity Sensor](https://shop.pimoroni.com/products/bme280-breakout?variant=29420960677971)
- [LM393 Soil Moisture Sensor](https://www.aliexpress.us/item/2255800833407262.html?spm=a2g0o.productlist.main.9.367d667aYKU6Z0&algo_pvid=4d439815-39e6-4d17-bab6-f4ec26b7cdea&algo_exp_id=4d439815-39e6-4d17-bab6-f4ec26b7cdea-4&pdp_npi=4%40dis%21USD%210.77%210.77%21%21%210.77%210.77%21%402101c5a417254760710065718e918f%2110000013531142169%21sea%21US%210%21ABX&curPageLogUid=joRIm1rxpy2O&utparam-url=scene%3Asearch%7Cquery_from%3A)
- [12V 24V 1 Channel Relay Board](https://www.aliexpress.us/item/3256807446915759.html?spm=a2g0o.productlist.main.17.262b2d23PYOvav&algo_pvid=c991661f-0e7c-477d-aae9-95ba2186eb6e&algo_exp_id=c991661f-0e7c-477d-aae9-95ba2186eb6e-8&pdp_npi=4%40dis%21USD%210.53%210.42%21%21%210.53%210.42%21%402101fb1517254761420073664ea7bf%2112000041581096962%21sea%21US%210%21ABX&curPageLogUid=XtaWh7AqB7gT&utparam-url=scene%3Asearch%7Cquery_from%3A)
- [12V DC Power Supply](https://www.aliexpress.us/item/2255799933908840.html?spm=a2g0o.productlist.main.9.665586b0vmNr9M&algo_pvid=3550904a-bac9-49ab-a6f2-d9db985ccdef&algo_exp_id=3550904a-bac9-49ab-a6f2-d9db985ccdef-4&pdp_npi=4%40dis%21USD%212.00%211.88%21%21%212.00%211.88%21%402101fb1317254762006988479eabfb%2110000000330370059%21sea%21US%210%21ABX&curPageLogUid=jFTTb4TPeuAz&utparam-url=scene%3Asearch%7Cquery_from%3A)
- 5V Power Supply
- [DC Connector](https://www.aliexpress.us/item/3256807391340344.html?spm=a2g0o.productlist.main.19.77d94db1sKkNvS&algo_pvid=103913fa-9fb1-4fb8-8010-1b2a016a2a03&algo_exp_id=103913fa-9fb1-4fb8-8010-1b2a016a2a03-9&pdp_npi=4%40dis%21USD%211.11%210.99%21%21%211.11%210.99%21%402103080617254763648465452edcd1%2112000041366272699%21sea%21US%210%21ABX&curPageLogUid=3ER9ts9xAM3E&utparam-url=scene%3Asearch%7Cquery_from%3A)
- [12V Pump](https://www.aliexpress.us/item/3256807267531113.html?spm=a2g0o.productlist.main.13.692571cemKWkOb&algo_pvid=f23c4c8a-0987-43f0-9a8a-154f61e52b93&algo_exp_id=f23c4c8a-0987-43f0-9a8a-154f61e52b93-6&pdp_npi=4%40dis%21USD%214.81%210.99%21%21%2134.07%217.03%21%402101e5c517254763964964603eb976%2112000040824628290%21sea%21US%210%21ABX&curPageLogUid=t9M07m5dkA6N&utparam-url=scene%3Asearch%7Cquery_from%3A)
- Switch
- Retention Switch
- Wire

### Features
-   Measure environmental conditions: temperature and humidity
-   Measure soil moisture
-   Control the pump to automatically water the plants
-   Display the current state of the measurements on a screen
-   Confirm the watering frequency and general configs with simple inputs
-   Start working just after I plug it

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mlucchelli/pico-sprout.git
   ```
2. Upload to Pico: Use a tool like [Thonny](https://core-electronics.com.au/guides/how-to-setup-a-raspberry-pi-pico-and-code-with-thonny/) to upload the files to your Raspberry Pico.

### Usage
- Power your Raspberry Pico: Once all the connections are made, power up the Pico.
- Live Monitoring: If you have connected a display, you’ll see real-time data from the sensors.
- Automated Watering: The system will automatically water your plants when the soil moisture drops below the threshold.

## Hardware Setup
Raspberry Pi Pico Pin Connections:
```bash
    BME 280: sda_pin=GP2, scl_pin=GP3

    LM393 Soil moisture: sensorA.do=GP27, sensorB.do=GP28

    Button: pin=GP1

    RGBPotentiometer: sda_pin=GP12, scl_pin=GP13

    Pump Relay: pin=GP15

    Display: CS=GP17, SCK=GP18, MOSI=GP19, DC=GP16, BL=GP20
```

### Wiring
![image](https://github.com/user-attachments/assets/68a1d961-dbc7-4aae-b38b-e9da23acfd7e)

## Code Structure
This system integrates sensors, controllers, and operational modes to provide an effective and adaptive irrigation solution.
### Core Components
#### Controllers
Controllers are responsible for managing specific hardware components and encapsulating their interaction logic.
- ```EnvironmentSensorController``` Manages the BME280 sensor.
- ```SoilSensorController``` Interfaces with soil moisture sensors.
- ```PotentiometerController``` Adjusts system parameters like watering frequency based on user input from the potentiometer.
- ```ButtonController``` Handles user input from physical buttons.
- ```PumpController``` Controls the water pump via a relay.

#### Modes
Modes represent different operational states of the system, each focusing on a specific aspect of user interaction. They manage how data is processed and presented, and how system components interact.
- ```CoreMode``` Acts as the central hub, integrating all other modes and managing the overall system state.
- ```EnvironmentMode``` Displays real-time environmental data (temperature and humidity) from the EnvironmentSensorController on the LCD.
- ```SoilMode``` Focuses on soil moisture readings and allows the user to view and adjust moisture reads.
- ```PumpMode``` Manages and configure the operation of the water pumpVersion 1: the protoboard.
  ![final_1](https://github.com/user-attachments/assets/37c2c56d-47d9-4cd6-b52d-a1e9b92cc3e0)


## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them.
Create a pull request with a clear description of your changes.

###License
This project is licensed under the MIT License.

