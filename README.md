# ESP32 LoRa IoT Application

## Overview

This project implements a simple IoT application using ESP32 LoRa devices programmed with MicroPython. The application demonstrates long-range communication between devices, displays critical information on an OLED screen, and sets up a basic web server for data management and visualization.

## Features

- Wi-Fi connectivity
- NTP time synchronization
- OLED display for showing device IP and current time
- LoRa communication for sending and receiving data packets
- Data logging with file size management
- Web server for displaying logged data

## Hardware Requirements

- ESP32-S3 LoRa device
- OLED display (SSD1306)
- USB cable for programming and power

## Software Requirements

- MicroPython firmware for ESP32-S3
- Thonny IDE (or any MicroPython-compatible IDE)
- Required libraries: `ssd1306`, `sx127x`

## Setup Instructions

1. **Flash MicroPython Firmware**
   - Download the latest MicroPython firmware for ESP32-S3 from [micropython.org](https://micropython.org/download/ESP32_GENERIC_S3/)
   - Erase the ESP32 flash:
     ```
     esptool.py --chip esp32s3 erase_flash
     ```
   - Flash the new firmware:
     ```
     esptool.py --chip esp32s3 --baud 460800 write_flash -z 0x0 esp32s3-XXXXXXXX.bin
     ```
     Replace `XXXXXXXX` with the actual firmware version.

2. **Install Required Libraries**
   - Connect to your ESP32 using Thonny IDE
   - Use Tools > Manage packages to install `ssd1306`
   - Manually install the `sx127x` library for LoRa functionality

3. **Configure the Application**
   - Open `main.py` in your IDE
   - Update the Wi-Fi credentials:
     ```python
     SSID = 'your_wifi_ssid'
     PASSWORD = 'your_wifi_password'
     ```
   - Adjust pin configurations if necessary to match your hardware setup

4. **Upload the Code**
   - Save the modified `main.py` to your ESP32 device

## Running the Application

1. Power on your ESP32 device
2. The device will automatically:
   - Connect to Wi-Fi
   - Synchronize time with an NTP server
   - Display IP and time on the OLED screen
   - Start the LoRa communication loop
   - Launch a web server for data visualization

3. To view logged data, connect to the same Wi-Fi network as the ESP32 and navigate to `http://<ESP32-IP-ADDRESS>` in a web browser

## Troubleshooting

- If the device fails to connect to Wi-Fi, check your credentials and network availability
- For LoRa communication issues, ensure proper wiring and antenna connection
- If the OLED display is not working, verify I2C connections and address

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your improvements.

## License

This project is open-source and available under the MIT License.

## Acknowledgements

- MicroPython community for firmware and libraries
- Espressif for the ESP32-S3 hardware
- Contributors to the `ssd1306` and `sx127x` libraries
