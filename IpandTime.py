from machine import Pin, I2C
import ssd1306
import time
import network
import ntptime

# Initialize and reset OLED
reset_pin = Pin(21, Pin.OUT)
reset_pin.value(0)
time.sleep(0.1)
reset_pin.value(1)

# Initialize I2C
i2c = I2C(0, scl=Pin(18), sda=Pin(17))

# Scan for I2C devices
devices = i2c.scan()

# Function to get IP address
def get_ip():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect('your_ssid', 'your_password')
    while not wlan.isconnected():
        pass
    return wlan.ifconfig()[0]

# Function to get current time with timezone offset
def get_time(timezone_offset):
    ntptime.settime()
    current_time = time.localtime(time.time() + timezone_offset * 3600)
    return "{:02}:{:02}:{:02}".format(current_time[3], current_time[4], current_time[5])

if devices:
    try:
        oled = ssd1306.SSD1306_I2C(128, 64, i2c)
        oled.fill(0)
        
        # Get IP address and time
        ip = get_ip()
        timezone_offset = -5  # Adjust this to your local timezone offset from UTC
        current_time = get_time(timezone_offset)
        
        # Display IP address and time on OLED
        oled.text('IP: ' + ip, 0, 0)
        oled.text('Time: ' + current_time, 0, 10)
        
        # Draw some graphics
        oled.rect(0, 20, 128, 44, 1)
        oled.line(0, 20, 128, 64, 1)
        oled.line(0, 64, 128, 20, 1)
        
        oled.show()
    except Exception as e:
        print('Error initializing OLED:', e)
else:
    print('No I2C devices found.')
